import unittest
from serializer.factory import Parser


class TomlTestCase(unittest.TestCase):

    def setUp(self):
        self.serializer = Parser.create_parser("toml")

    def test_float_toml(self):
        expected_result = "15.2"
        result = self.serializer.dumps(expected_result)
        fresult = self.serializer.loads(result)
        self.assertEqual(fresult, expected_result)

    def test_string_list_toml(self):
        expected_result = ["hello", "good", "nice"]
        result = self.serializer.dumps(expected_result)
        fresult = self.serializer.loads(result)
        self.assertEqual(fresult, expected_result)

    def test_int_toml(self):
        expected_result = "40"
        result = self.serializer.dumps(expected_result)
        fresult = self.serializer.loads(result)
        self.assertEqual(fresult, expected_result)

    def test_list_toml(self):
        expected_result = [1, 2, 3]
        result = self.serializer.dumps(expected_result)
        fresult = self.serializer.loads(result)
        self.assertEqual(fresult, expected_result)

    def test_bytes_toml(self):
        expected_result = bytes(b'd\x00S\x01')
        result = self.serializer.dumps(expected_result)
        fresult = self.serializer.loads(result)
        self.assertEqual(fresult, expected_result)

    def test_tuple_toml(self):
        expected_result = (1, 2, 3)
        result = self.serializer.dumps(expected_result)
        fresult = self.serializer.loads(result)
        self.assertEqual(fresult, expected_result)

    if __name__ == "__main__":
        unittest.main()
