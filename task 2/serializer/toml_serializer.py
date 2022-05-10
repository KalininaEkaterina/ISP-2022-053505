from serializer.serializer import Serializer
def serialize_toml(obj) -> str:
    if type(obj) == tuple:
        ans = ""
        for i in obj:
            ans += f"{serialize_toml(i)}, "
        return f"[ {ans[0:len(ans) - 1]}]"
    else:
        return f"\"{str(obj)}\"".replace("\n", "\\n")


def deserialize_toml(obj: str):
    if obj == '[]':
        return tuple()
    elif obj[0] == '[':
        obj = obj[1:len(obj) - 1]
        parsed = []
        depth = 0
        quote = False
        substr = ""
        for i in obj:
            if i == '[':
                depth += 1
            elif i == ']':
                depth -= 1
            elif i == '\"':
                quote = not quote
            elif i == ',' and not quote and depth == 0:
                parsed.append(deserialize_toml(substr))
                substr = ""
                continue
            elif i == ' ' and not quote:
                continue

            substr += i

        return tuple(parsed)
    else:
        return obj[1:len(obj) - 1]


class TomlSerializer:

    @staticmethod
    def dumps(obj) -> str:
        obj = Serializer.serialize(obj)
        return f"tuple = {serialize_toml(obj)}"

    @staticmethod
    def dump(obj, file):
        file.write(TomlSerializer.dumps(obj))

    @staticmethod
    def loads(obj: str):
        obj = obj.split('=', 1)[1]

        obj = deserialize_toml(obj.replace("\\n", "\n").strip())
        return Serializer.deserialize(obj)

    @staticmethod
    def load(file):
        return TomlSerializer.loads(file.read())
