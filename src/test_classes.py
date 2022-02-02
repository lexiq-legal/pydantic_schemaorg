import importlib
import inspect
import json
import os
import re
from collections import Iterator
from typing import Dict, List, Union

import requests
from requests import Response

dir = os.path.dirname(__file__)
dir = f"{dir}/../pydantic_schemaorg"
files = os.listdir(f"{dir}")


def get_modules_in_package(dir_name: str, package_name: str):
    files = os.listdir(dir_name)
    for file in files:
        if file not in ["__init__.py", "__pycache__"]:
            if file[-3:] != ".py":
                continue
            file_name = file[:-3]
            module_name = package_name + "." + file_name
            for name, cls in inspect.getmembers(
                    importlib.import_module(module_name), inspect.isclass
            ):
                if cls.__module__ == module_name:
                    yield cls


def get_all_examples() -> Iterator[Union[List, Dict]]:
    schema_org_request: Response = requests.get(
        "https://schema.org/version/latest/schemaorg-all-examples.txt"
    )
    content = schema_org_request.text
    matches = re.findall(r'<script type\="application/ld\+json">(?P<json_ld>.*?)</script>', content,
                         flags=re.DOTALL | re.M)
    for match in matches:
        m = match
        m = m.replace('\n', '')
        b = json.loads(m)
        yield b


for example in get_all_examples():
    if type(example) == dict and type(example.get('@type')) != list:
        type_ = example.get('@type','').split(':')[-1]
        if not type_:
            print(f'Not a type: {type_}')
            continue
        try:
            mod = __import__(f'pydantic_schemaorg.{type_}', fromlist=[f'{type_}'])
            class_ = getattr(mod, f'{type_}')
            model = class_.__call__(**example)
            print(f'Success for {type_}', model.json())
        except Exception as e:
            print(f'Exception for type {type_}', e)

for module in get_modules_in_package(dir, "pydantic_schemaorg"):
    module._update_all_fields()
    module.__call__()
