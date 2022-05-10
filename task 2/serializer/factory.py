from serializer.json_serializer import JsonSerializer
from serializer.yaml_serializer import YamlSerializer
from serializer.toml_serializer import TomlSerializer


class Parser:

    def create_parser(name: str):
        name = name.lower()
        if name == "json":
            return JsonSerializer()
        elif name == "yaml":
            return YamlSerializer()
        elif name == "toml":
            return TomlSerializer()
        else:
            raise ValueError