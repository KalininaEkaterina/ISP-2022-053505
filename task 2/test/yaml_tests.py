import math
import maintest
import unittest
from serializer.factory import Parser


class YamlTestCase(unittest.TestCase):

    def setUp(self):
        self.serializer = Parser.create_parser("yaml")

    def test_float_yaml(self):
        expected_result = "15.2"
        result = self.serializer.dumps(expected_result)
        fresult = self.serializer.loads(result)
        self.assertEqual(fresult, expected_result)

    def test_string_list_yaml(self):
        expected_result = ["hello", "good", "nice"]
        result = self.serializer.dumps(expected_result)
        fresult = self.serializer.loads(result)
        self.assertEqual(fresult, expected_result)

    def test_int_yaml(self):
        expected_result = "40"
        result = self.serializer.dumps(expected_result)
        fresult = self.serializer.loads(result)
        self.assertEqual(fresult, expected_result)

    def test_main(self):
        ser = self.serializer.dumps(maintest.f(3))
        deser = self.serializer.loads(ser)
        self.assertEqual(maintest.f(3), deser)

    def test_list_yaml(self):
        expected_result = [1, 2, 3]
        result = self.serializer.dumps(expected_result)
        fresult = self.serializer.loads(result)
        self.assertEqual(fresult, expected_result)

    def test_bytes_yaml(self):
        expected_result = bytes(b'd\x00S\x01')
        result = self.serializer.dumps(expected_result)
        fresult = self.serializer.loads(result)
        self.assertEqual(fresult, expected_result)

    def test_tuple_yaml(self):
        expected_result = (1, 2, 3)
        result = self.serializer.dumps(expected_result)
        fresult = self.serializer.loads(result)
        self.assertEqual(fresult, expected_result)

    if __name__ == "__main__":
        unittest.main()
