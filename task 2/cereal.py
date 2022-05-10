from __future__ import annotations

import code
import sys
import importlib
from argparser.argparser import ArgParser
from serializer import (
    Serializer,
    JsonSerializer,
    YamlSerializer,
    TomlSerializer
)

items_to_dump, items_to_load, items_to_convert = ArgParser.get_args()


def get_fabric(filename: str) -> Serializer | None:
    filetype = filename.lower().split('.')[-1]
    fabrics = {
        'json': JsonSerializer,
        'yaml': YamlSerializer,
        'toml': TomlSerializer
    }
    return fabrics.get(filetype, None)


def load(filename: str) -> any:
    fabric = get_fabric(filename)
    if fabric is None:
        return None
    serializer = fabric.create_serializer()
    item = serializer.load(filename)
    return item


def dumpobjects(inputstrings):
    """Dump obj from string."""
    def get_object(filename: str, obj_name):
        module_name = filename.removesuffix('.py').split('/')[-1]
        module_path = filename.removesuffix(f'{module_name}.py')
        sys.path.append(module_path)

        sys.stdout = None
        mod = importlib.import_module(module_name)
        sys.stdout = sys.__stdout__

        item = mod.__dict__[obj_name]

        return item

    def dump(item, filename: str) -> any:
        fabric = get_fabric(filename)
        if fabric is None:
            return None
        serializer = fabric.create_serializer()
        serializer.dump(item, filename)
        item = serializer.load(filename)
        return item

    def parceinputstr(inputstr: str):
        filename, _, temp = inputstr.partition(':')
        obj_name, _, file_format = temp.partition(':')
        return (filename, obj_name, file_format)

    for inputstr in inputstrings:
        filename, obj_name, file_format = parceinputstr(inputstr)
        try:
            item = get_object(filename, obj_name)
            dump(item, f'{obj_name}.{file_format}')
            print(f'{inputstr} dumped to {obj_name}.{file_format}')
        except KeyError as key_error:
            print(f"Error when dumping {inputstr}: {key_error} doesn't exists")


def loadfiles(files_to_load):
    """Load obj from file."""

    for filename in files_to_load:
        obj_name = filename.split('.')[-2]
        try:
            locals().update({obj_name: load(filename)})
            print(f'{obj_name} loaded from {filename}')
        except FileNotFoundError:
            print(f'{filename}: No such file')

    code.interact(local=locals(),
                  banner='prompt', exitmsg='')


def convertfiles(files_to_convert: list[str]) -> None:

    def convert(filename: str, filetype: str):
        item = load(filename)
        name = filename.split('.')[0]
        out_serializer = get_fabric(filetype).create_serializer()
        out_serializer.dump(item, f'{name}.{filetype}')
        print(f"{filename} converted to {name}.{filetype}")

    filetypes = list(
        filter(lambda file: file.find('.') == -1, files_to_convert))
    start = 0
    end = 0

    for filetype in filetypes:
        end = files_to_convert.index(filetype, start)
        for i in range(start, end):
            convert(files_to_convert[i], filetype)
        start = end + 1


if items_to_dump is not None:
    dumpobjects(items_to_dump)

if items_to_convert is not None:
    convertfiles(items_to_convert)

if items_to_load is not None:
    loadfiles(items_to_load)

if items_to_convert is items_to_dump and items_to_load is None:
    ArgParser.print_help()