import importlib
import inspect
import os

dir = os.path.dirname(__file__)
dir = f'{dir}/../pydantic_schemaorg'
files = os.listdir(f'{dir}')
print(files)

def get_modules_in_package(dir_name:str,package_name: str):
    files = os.listdir(dir_name)
    for file in files:
        if file not in ['__init__.py', '__pycache__']:
            if file[-3:] != '.py':
                continue
            file_name = file[:-3]
            module_name = package_name + '.' + file_name
            for name, cls in inspect.getmembers(importlib.import_module(module_name), inspect.isclass):
                if cls.__module__ == module_name:
                    yield cls

for module in get_modules_in_package(dir, 'pydantic_schemaorg'):
    module.__call__()