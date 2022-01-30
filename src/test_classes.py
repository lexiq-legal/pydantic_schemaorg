import html
import importlib
import inspect
import json
import os
import re
from http.client import HTTPResponse
from re import Match

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


def get_all_examples():
    schema_org_request: Response = requests.get(
        "https://schema.org/version/latest/schemaorg-all-examples.txt"
    )
    content=schema_org_request.text
    reg=re.compile(r'<script type="application/ld+json">')
    t=re.match(r'</script>','</script>')
    matches=re.findall(r'<script type\="application/ld\+json">(?P<json_ld>.*?)</script>',content,flags=re.DOTALL|re.M)
    for match in matches:
        m=match
        m=m.replace('\n','')
        b=json.loads(m)
        print(b)

# for module in get_modules_in_package(dir, "pydantic_schemaorg"):
#     module.__call__()

get_all_examples()
