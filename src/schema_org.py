import datetime
import os
from pathlib import Path
from typing import Dict, Union, Set, List, Tuple, Callable

import jinja2

from constants import data_type_map, PACKAGE_NAME
from jinja import jinja_env, python_safe
from models import PydanticClass, PydanticField, Import


class SchemaOrg:
    def __init__(
            self,
            schema_org: Dict[str, Dict],
            type_map: Dict[str, tuple],
            type_specificity: Dict[str, int],
    ):
        self.schema_org = schema_org
        self.pydantic_classes: Dict[str, Union[PydanticClass, tuple]] = dict()
        self._type_specificity = dict(type_specificity)
        self.pydantic_fields = {k: {} for k in data_type_map}

    def get_all_classes(self):
        return [
            k.strip().split(":")[-1]
            for k, v in self.schema_org.items()
            if v["@type"] != "rdf:Property"
        ]

    def get_class_by_name(self, name: str) -> Dict:
        return self.schema_org[f"schema:{name}"]

    @staticmethod
    def update_imports(
            imports: List[Import], class_path: str, classes_: set, type: str
    ) -> List[Import]:
        filter_func: Callable[[Import], bool] = (
            lambda i: i.classPath == class_path and i.type == type
        )
        import_ = next(filter(filter_func, imports), None)
        if not import_:
            imports.append(Import(type=type, classPath=class_path, classes_=classes_))
        else:
            import_.classes_.update(classes_)
        return imports

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
        return [
            incl_type.strip().split(":")[-1]
            for incl_type in self._to_set(field.get("schema:rangeIncludes"))
        ]

    # Return all fields that belong to model
    def _fields_for_model(self, name: str) -> List[Tuple[str, Dict]]:
        return [
            (key.strip().split(":")[-1], field)
            for key, field in self.schema_org.items()
            if (
                    field.get("@type") == "rdf:Property"
                    and f"schema:{name}" in self._to_set(field.get("schema:domainIncludes"))
            )
        ]

    # TODO: refactor this ugly code
    def extract_fields(self, name: str) -> (List[PydanticField], List[Import]):
        fields: List[PydanticField] = []
        imports = self._get_default_imports()
        for key, field in self._fields_for_model(name):
            field_parent_types = self._get_including_types(field)

            field_types = [type_name for type_name in field_parent_types]
            pydantic_types = ()
            for field_type in sorted(
                    field_types,
                    key=lambda ft: self._type_specificity.get(ft, 0),
                    reverse=True,
            ):
                if field_type in data_type_map:
                    pydantic_types += (data_type_map[field_type][0],)
                    if data_type_map[field_type][1]:
                        imports = self.update_imports(
                            imports,
                            class_path=f"{data_type_map[field_type][1]}",
                            classes_={data_type_map[field_type][2]},
                            type="field",
                        )

                else:
                    if name != field_type:
                        imports = self.update_imports(
                            imports,
                            class_path=f"{PACKAGE_NAME}.{field_type}",
                            classes_={field_type},
                            type="field",
                        )
                        pydantic_types += (field_type,)
                    else:  # if type is self-reference
                        pydantic_types += (f"'{field_type}'",)

            if field_parent_types != field_types:
                pydantic_types = pydantic_types + ("Any",)

            if not "str" in pydantic_types:
                pydantic_types += ("str",)

            type_tuple = ", ".join(pydantic_types)

            if not pydantic_types:
                continue
            elif len(pydantic_types) > 1:
                imports = self.update_imports(
                    imports,
                    class_path="typing",
                    classes_={"List", "Union", "Optional"},
                    type="field",
                )
                optional = pydantic_types[-1] != "Any"
                pydantic_types = (
                    f"Union[List[Union[{type_tuple}]], Union[{type_tuple}]]"
                )
                if optional:
                    pydantic_types = f"Optional[{pydantic_types}]"
            else:
                imports = self.update_imports(
                    imports,
                    class_path="typing",
                    classes_={"List", "Union", "Optional", "Any"},
                    type="field",
                )
                pydantic_types = (
                    type_tuple
                    if type_tuple == "Any"
                    else f"Optional[Union[List[{type_tuple}], {type_tuple}]]"
                )
            fields.append(
                PydanticField(
                    name=key,
                    description=self.cast_description(
                        self.schema_org[f"schema:{key}"].get("rdfs:comment", "")
                    ),
                    type=pydantic_types,
                )
            )
        return fields, imports

    def load_type(self, name: str) -> PydanticClass:
        if name in self.pydantic_classes:
            print(f"{name} exists, skipping..")
            return self.pydantic_classes[name]
        try:
            node = self.get_class_by_name(name)
        except KeyError:
            raise ValueError(f"Model {name} does not exist")

        fields, imports = self.extract_fields(name)
        parent_names, forward_refs, depth = self.extract_parents(node)

        for parent_name in parent_names:
            imports = self.update_imports(
                imports,
                class_path=f"{PACKAGE_NAME}.{parent_name}",
                classes_={parent_name},
                type="parent",
            )

        self.pydantic_classes[name] = PydanticClass(
            name=name,
            description=self.cast_description(node.get("rdfs:comment", "")),
            fields=list(fields),
            parents=[f'{parent_name}' for parent_name in parent_names],
            parent_imports=list(filter(lambda x: x.type == 'parent', imports)),
            depth=depth,
            field_imports=list(filter(lambda x: x.type == 'field', imports)),
            forward_refs=forward_refs
        )

        with open(f"{PACKAGE_NAME}/{self.pydantic_classes[name].valid_name}.py", "w") as model_file:
            with open(
                    Path(__file__).parent / "templates/model.py.tpl"
            ) as template_file:
                template = jinja_env.from_string(template_file.read())

                template_args = dict(
                    schemaorg_version=os.getenv("SCHEMAORG_VERSION"),
                    commit=os.getenv("COMMIT"),
                    jinja2_version=jinja2.__version__,
                    timestamp=datetime.datetime.now(),
                    model=self.pydantic_classes[name],
                )
            template.stream(**template_args).dump(model_file)
        return self.pydantic_classes[name]

    @staticmethod
    def _filter_forward_refs(forward_refs: List[Import]) -> List[Import]:
        a: Dict[str, Union[set, None]] = {}
        for forward_ref in forward_refs:
            if a.get(forward_ref.classPath, None):
                a[forward_ref.classPath].update(forward_ref.classes_)
            else:
                a[forward_ref.classPath] = forward_ref.classes_
        return [Import(type='forward_ref', classPath=k, classes_=v) for k, v in a.items()]

    def extract_parents(self, node) -> (set, list, int):
        parent_names = set(
            reference.strip().split(":")[-1]
            for reference in self._to_set(node.get("rdfs:subClassOf", []))
        )

        node_types = node["@type"] if type(node["@type"]) == list else [node["@type"]]

        for node_type in node_types:
            if node_type.startswith("schema:"):
                parent_names.add(node_type.strip().split(":")[-1])

        parents: List[PydanticClass] = []
        forward_refs = []
        for parent_name in parent_names:
            parent = self.load_type(parent_name)
            parents.append(self.load_type(parent_name))
            forward_refs += parent.field_imports + parent.forward_refs

        parent_depth = next(
            map(lambda y: y.depth, sorted(parents, key=lambda x: x.depth)), 0
        )
        sorted_parents = list(
            map(
                lambda y: y.valid_name,
                sorted(parents, key=lambda x: x.depth, reverse=True),
            )
        )
        depth = parent_depth + 1

        if not sorted_parents:
            sorted_parents = {"SchemaOrgBase"}

        return sorted_parents, self._filter_forward_refs(forward_refs), depth

    @staticmethod
    def _get_default_imports() -> List[Import]:
        return [Import(classes_={"Field"}, classPath="pydantic", type="parent")]

    def write_init(self):
        with open(f"{PACKAGE_NAME}/__init__.py", "w") as init_file:
            with open(
                    Path(__file__).parent / "templates/__init__.py.tpl"
            ) as template_file:
                template = jinja_env.from_string(template_file.read())

                template_args = dict(
                    schemaorg_version=os.getenv("SCHEMAORG_VERSION"),
                    commit=os.getenv("COMMIT"),
                    jinja2_version=jinja2.__version__,
                    timestamp=datetime.datetime.now(),
                    all_classes=sorted(self.pydantic_classes.values(),key=lambda x: x.depth),
                )
            template.stream(**template_args).dump(init_file)
