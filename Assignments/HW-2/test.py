from main import JSON
import unittest
from parameterized import parameterized
import json


class JsonTestCase(unittest.TestCase):
    def setUp(self):
        self.filepath = "C:\\Users\\matthew.kuilan\\Downloads\\test-file.json"
        initial_data = {"name": "Alice", "email": "Alice@example.com"}

        with open(self.filepath, 'w') as file:
            json.dump(initial_data, file, indent=4)

        self.instance = JSON(self.filepath)

    @parameterized.expand([
        ("test_case_1", 'height', 'height'),
        ("test_case_2", 'address', 'address'),
        ("test_case_3", 'DOB', 'DOB'),

    ])
    
    def test_add_field(self, name, key, expected):
        self.instance.add_field(key)
        self.assertIn(expected, self.instance.jdict)
        print(name, self.instance.jdict)
    
    def test_update_field(self):
        self.instance.add_field('height')
        self.assertIn('height', self.instance.jdict)

    def test_update_value(self):
        self.instance.add_value('height', 6.5)
        self.assertEqual(self.instance.jdict['height'], 6.3)


if __name__ == '__main__':
    unittest.main()