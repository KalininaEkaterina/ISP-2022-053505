import unittest
from serializer.factory import Parser


class JsonTestCase(unittest.TestCase):

    def setUp(self):
        self.serializer = Parser.create_parser("json")

    def test_float_json(self):
        expected_result = "15.2"
        result = self.serializer.dumps(expected_result)
        fresult = self.serializer.loads(result)
        self.assertEqual(fresult, expected_result)

    def test_string_list_json(self):
        expected_result = ["hello", "good", "nice"]
        result = self.serializer.dumps(expected_result)
        fresult = self.serializer.loads(result)
        self.assertEqual(fresult, expected_result)

    def test_int_json(self):
        expected_result = "40"
        result = self.serializer.dumps(expected_result)
        fresult = self.serializer.loads(result)
        self.assertEqual(fresult, expected_result)

    def test_list_json(self):
        expected_result = [1, 2, 3]
        result = self.serializer.dumps(expected_result)
        fresult = self.serializer.loads(result)
        self.assertEqual(fresult, expected_result)

    def test_bytes_json(self):
        expected_result = bytes(b'd\x00S\x01')
        result = self.serializer.dumps(expected_result)
        fresult = self.serializer.loads(result)
        self.assertEqual(fresult, expected_result)

    def test_tuple_json(self):
        expected_result = (1, 2, 3)
        result = self.serializer.dumps(expected_result)
        fresult = self.serializer.loads(result)
        self.assertEqual(fresult, expected_result)

    if __name__ == "__main__":
        unittest.main()
