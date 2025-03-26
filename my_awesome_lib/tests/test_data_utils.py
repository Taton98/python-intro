import unittest
from my_awesome_lib.data_utils import json_to_dict, dict_to_json

class TestDataUtils(unittest.TestCase):
    def test_json_to_dict(self):
        self.assertEqual(json_to_dict('{"key": "value"}'), {"key": "value"})
        self.assertIsNone(json_to_dict("invalid json"))

    def test_dict_to_json(self):
        self.assertEqual(dict_to_json({"key": "value"}), '{\n    "key": "value"\n}')

if __name__ == "__main__":
    unittest.main()
