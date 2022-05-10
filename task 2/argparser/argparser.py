import argparse

class ArgParser:

    @staticmethod
    def parse():
        parser = argparse.ArgumentParser()
        parser.add_argument('-l', '--load', dest="l", nargs='+')
        parser.add_argument('-d', '--dump', dest="d", nargs='+')
        parser.add_argument('-c', '--config', dest="c", nargs='?', default=None)
        return parser.parse_args()

    @staticmethod
    def load_from() -> list[str]:
        args = ArgParser.parse()
        return args.l

    @staticmethod
    def dump_in() -> list[str]:
        args = ArgParser.parse()
        return args.d

    @staticmethod
    def getargs():
        args = ArgParser.parse()

        if args.c is not None:
            args.l, args.d = ArgParser.get_config(str(args.c))

        return args.d, args.l

    @staticmethod
    def get_config(config: str) -> list[str]:
        try:
            file = open(config, "r")
            configs = file.read()
        except Exception as e:
            print(e)
        finally:
            file.close()
            return configs.split("\n")