import datetime
import json
import os
import shutil
from http.client import HTTPResponse
from pathlib import Path
from urllib import request

from constants import data_type_map, PACKAGE_NAME, data_type_specificity
from jinja import jinja_env
from schema_org import SchemaOrg


def write_base_class():
    with open(f'{PACKAGE_NAME}/SchemaOrgBase.py', 'w') as model_file:
        with open(Path(__file__).parent / "templates/schema_org_base.py.tpl") as template_file:
            template = jinja_env.from_string(template_file.read())
            template_args = dict(
                schemaorg_version=os.getenv("SCHEMAORG_VERSION"),
                commit=os.getenv("COMMIT"),
                timestamp=datetime.datetime.now()
            )
        template.stream(**template_args).dump(model_file)


def init_package():
    shutil.rmtree(PACKAGE_NAME)
    os.makedirs(PACKAGE_NAME, exist_ok=True)
    with open(f'{PACKAGE_NAME}/__init__.py', 'w') as model_file:
        with open(Path(__file__).parent / "templates/__init__.py.tpl") as template_file:
            open(f'{PACKAGE_NAME}/__init__.py', 'w')
            template = jinja_env.from_string(template_file.read())
            template_args = dict(
                schemaorg_version=os.getenv("SCHEMAORG_VERSION"),
                commit=os.getenv("COMMIT"),
                timestamp=datetime.datetime.now()
            )
        template.stream(**template_args).dump(model_file)


if __name__ == "__main__":
    init_package()
    write_base_class()
    schema_org_request: HTTPResponse = request.urlopen(
        'https://schema.org/version/latest/schemaorg-current-https.jsonld')
    schema_data = json.loads(schema_org_request.read().decode('utf-8'))
    schema_data = {node["@id"]: node for node in schema_data["@graph"]}
    schema_org_api = SchemaOrg(
        schema_data,
        data_type_map,
        data_type_specificity
    )
    for class_ in schema_org_api.get_all_classes():
        schema_org_api.load_type(class_)
