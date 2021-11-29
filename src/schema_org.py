import datetime
import os
from pathlib import Path
from typing import Dict, Union, Set, List, Tuple

import jinja2

from constants import data_type_map, PACKAGE_NAME
from jinja import jinja_env
from models import PydanticClass, PydanticField


class SchemaOrg:
    def __init__(
            self,
            schema_org: Dict[str, Dict],
            type_map: Dict[str, tuple],
            type_specificity: Dict[str, int]
    ):
        self.schema_org = schema_org
        self.pydantic_classes: Dict[str, Union[PydanticClass, tuple]] = dict(type_map)
        self._type_specificity = dict(type_specificity)
        self.pydantic_fields = {k: {} for k in data_type_map}

    def get_all_classes(self):
        return [
            k.strip().split(":")[-1]
            for k, v in self.schema_org.items()
            if v["@type"] != "rdf:Property"
        ]

    @staticmethod
    def _to_set(_object, prop="@id") -> Set[str]:
        if isinstance(_object, list):
            return set(item[prop] if prop is not None else item for item in _object)
        elif _object is None:
            return set()
        else:
            return {_object[prop] if prop is not None else _object}

    @staticmethod
    def cast_description(description):
        return description if isinstance(description, str) else description["@value"]

    def _get_including_types(self, field: dict) -> List[str]:
        return [incl_type.strip().split(":")[-1] for incl_type in self._to_set(field.get("schema:rangeIncludes"))]

    # Return all fields that belong to model
    def _fields_for_model(self, name: str) -> List[Tuple[str, Dict]]:
        return [(key.strip().split(":")[-1], field)
                for key, field in self.schema_org.items() if (
                        field.get("@type") == "rdf:Property" and
                        f"schema:{name}" in self._to_set(field.get("schema:domainIncludes")))]

    def extract_fields(self, name: str):
        fields: List[PydanticField] = []
        imports = self._get_default_imports()
        for key, field in self._fields_for_model(name):
            field_parent_types = self._get_including_types(field)
            field_types = [type_name for type_name in field_parent_types if type_name in self.pydantic_classes]
            pydantic_types = ()
            for field_type in sorted(field_types, key=lambda ft: self._type_specificity.get(ft, 0),
                                     reverse=True):
                if field_type in data_type_map:
                    pydantic_types += (data_type_map[field_type][0],)
                else:
                    # this must be a generated class
                    imports.update({f'{PACKAGE_NAME}.{field_type}': {field_type}})
                    pydantic_types += (field_type,)

            for field_type in field_types:
                if field_type in data_type_map.keys() and data_type_map[field_type][1]:
                    if data_type_map[field_type][1] and data_type_map[field_type][1] not in imports.keys():
                        imports[data_type_map[field_type][1]] = set()
                    imports[data_type_map[field_type][1]].add(data_type_map[field_type][2])
            if field_parent_types != field_types:
                pydantic_types = pydantic_types + ("Any",)
            type_tuple = ", ".join(pydantic_types)

            if not pydantic_types:
                continue
            elif len(pydantic_types) > 1:
                imports.update({'typing': {'List', 'Union', 'Any', 'Optional'}})
                optional = pydantic_types[-1] != "Any"
                pydantic_types = f"Union[List[Union[{type_tuple}]], Union[{type_tuple}]]"
                if optional:
                    pydantic_types = f"Optional[{pydantic_types}]"
            else:
                imports.update({'typing': {'List', 'Union', 'Any', 'Optional'}})
                pydantic_types = (
                    type_tuple
                    if type_tuple == "Any"
                    else f"Optional[Union[List[{type_tuple}], {type_tuple}]]"
                )
            fields.append(PydanticField(
                name=key,
                description=self.cast_description(self.schema_org[f"schema:{key}"].get("rdfs:comment", "")),
                type=pydantic_types))
        return fields, imports

    def load_type(self, name: str):
        if name in self.pydantic_classes:
            print(f'{name} exists, skipping..')
            return
        try:
            node = self.schema_org[f"schema:{name}"]
        except KeyError:
            raise ValueError(f"Model {name} does not exist")

        fields, imports = self.extract_fields(name)
        parent_names = self.extract_parents(node)

        for parent_name in parent_names:
            imports.update({f'{PACKAGE_NAME}.{parent_name}': {parent_name}})

        self.pydantic_classes[name] = PydanticClass(
            name=name,
            description=self.cast_description(node.get("rdfs:comment", "")),
            fields=list(fields),
            parents=parent_names,
            imports=imports)

        with open(f'{PACKAGE_NAME}/{name}.py', 'w') as model_file:
            with open(Path(__file__).parent / "templates/model.py.tpl") as template_file:
                template = jinja_env.from_string(template_file.read())

                template_args = dict(
                    schemaorg_version=os.getenv("SCHEMAORG_VERSION"),
                    commit=os.getenv("COMMIT"),
                    jinja2_version=jinja2.__version__,
                    timestamp=datetime.datetime.now(),
                    model=self.pydantic_classes[name],
                )
            template.stream(**template_args).dump(model_file)

    def extract_parents(self, node) -> set:
        parent_names = set(
            reference.strip().split(":")[-1]
            for reference in self._to_set(node.get("rdfs:subClassOf", []))
        )

        node_types = node['@type'] if type(node['@type']) == list else [node['@type']]
        for node_type in node_types:
            if node_type.startswith('schema:'):
                parent_names.add(node_type.strip().split(":")[-1])

        for parent_name in parent_names:
            self.load_type(parent_name)

        if not parent_names:
            parent_names = {'SchemaOrgBase'}
        return parent_names

    @staticmethod
    def _get_default_imports() -> Dict[str, set]:
        return {'pydantic': {'Field'}}