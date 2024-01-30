import unittest
import os
import json
from calculator import Calculator
from utils import double

class TestFilesAndModules(unittest.TestCase):
    def test_create_file(self):
        with open("data.txt", "w") as file:
            file.write("Hello, world!")
        self.assertTrue(os.path.exists("data.txt"))

    def test_read_file(self):
        with open("data.txt", "r") as file:
            content = file.read()
        self.assertEqual(content, "Hello, world!")

    def test_append_to_file(self):
        with open("data.txt", "a") as file:
            file.write("\nAppended line")
        with open("data.txt", "r") as file:
            lines = file.readlines()
        self.assertEqual(lines[-1], "Appended line")

    def test_utils_module(self):
        self.assertEqual(double(5), 10)

    def test_double_function(self):
        self.assertEqual(double(10), 20)

    def test_create_and_move_directory(self):
        os.mkdir("data")
        os.rename("data.txt", "data/data.txt")
        self.assertTrue(os.path.exists("data/data.txt"))

    def test_remove_directory(self):
        os.rmdir("data")
        self.assertFalse(os.path.exists("data"))

    def test_create_json_file(self):
        data = {"name": "John", "age": 30}
        with open("data.json", "w") as file:
            json.dump(data, file)
        self.assertTrue(os.path.exists("data.json"))

    def test_read_json_file(self):
        with open("data.json", "r") as file:
            data = json.load(file)
        self.assertEqual(data["name"], "John")
        self.assertEqual(data["age"], 30)

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(10, 5), 15)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(10, 5), 50)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(10, 5), 2)

if __name__ == "__main__":
    unittest.main()
