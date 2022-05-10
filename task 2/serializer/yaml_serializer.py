from serializer.serializer import Serializer

def serialize_yaml(obj) -> str:
    if type(obj) == tuple:
        ans = "!!python/tuple"
        parsed = []
        if len(obj) == 0:
            return f"{ans} []"
        for i in obj:
            parsed.append(serialize_yaml(i).replace("\n", "\n  "))
        parsed.insert(0, ans)
        return "\n- ".join(parsed)
    else:
        if type(obj) == str and '\n' in obj:
            return f"\"{obj}\""
        else:
            return str(obj)




def deserialize_yaml(obj: str):
    splitted = obj.split("\n", 1)
    if splitted[0] == "!!python/tuple":
        splitted = splitted[1].split("\n")

        substr = ""
        parsed = []
        quote = False
        for i in splitted:
            if i == '' or quote:
                substr += f"\n{i}"
                if i != '' and i[len(i) - 1] == '\"':
                    quote = False
                    parsed.append(deserialize_yaml(substr))
                    substr = ""
                continue
            spacecount = len(i) - len(i.lstrip(' '))
            istr = i[2:]
            if istr[0] == '\"':
                if istr != "":
                    parsed.append(deserialize_yaml(substr))
                quote = True
                substr = f"\n{istr}"
                continue

            if spacecount == 0 and not quote:
                if substr == "":
                    substr = istr
                else:
                    parsed.append(deserialize_yaml(substr))
                    substr = istr
            else:
                substr += f"\n{istr}"
        parsed.append(deserialize_yaml(substr))
        return tuple(parsed)

    elif splitted[0] == "!!python/tuple []":
        return tuple()
    else:
        return str(obj)

class YamlSerializer:

    @staticmethod
    def dumps(obj) -> str:
        obj = Serializer.serialize(obj)
        return serialize_yaml(obj)

    @staticmethod
    def dump(obj, file):
        file.write(YamlSerializer.dumps(obj))

    @staticmethod
    def loads(obj: str):
        obj = deserialize_yaml(obj)
        return Serializer.deserialize(obj)

    @staticmethod
    def load(file):
        return YamlSerializer.loads(file.read())