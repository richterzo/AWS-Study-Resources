# test_variables_control_flow_functions.py

import unittest
from practice_1 import square, check_number, sum_numbers, count_vowels, is_palindrome

class TestFunctions(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(5), 25)
        self.assertEqual(square(-3), 9)
        self.assertEqual(square(0), 0)

    def test_check_number(self):
        self.assertEqual(check_number(5), "positivo")
        self.assertEqual(check_number(-3), "negativo")
        self.assertEqual(check_number(0), "zero")

    def test_sum_numbers(self):
        self.assertEqual(sum_numbers([1, 2, 3, 4, 5]), 15)
        self.assertEqual(sum_numbers([-1, 2, -3, 4, -5]), -3)
        self.assertEqual(sum_numbers([]), 0)

if __name__ == '__main__':
    unittest.main()
