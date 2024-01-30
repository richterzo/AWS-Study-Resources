import unittest
from practice_6 import *

class TestStringManipulation(unittest.TestCase):
    def test_convert_to_uppercase(self):
        self.assertEqual(convert_to_uppercase("hello"), "HELLO")

    def test_convert_to_lowercase(self):
        self.assertEqual(convert_to_lowercase("HELLO"), "hello")

    def test_count_substring_occurrences(self):
        self.assertEqual(count_substring_occurrences("hello hello hello", "hello"), 3)

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("radar"))
        self.assertFalse(is_palindrome("python"))

    def test_split_string(self):
        self.assertEqual(split_string("hello world"), ["hello", "world"])

    def test_join_words(self):
        self.assertEqual(join_words(["hello", "world"]), "hello world")

    def test_word_lengths(self):
        self.assertEqual(word_lengths("hello world"), [5, 5])

class TestFunctionalProgramming(unittest.TestCase):
    def test_filter_even_numbers(self):
        self.assertEqual(filter_even_numbers([1, 2, 3, 4, 5, 6]), [2, 4, 6])

    def test_double_elements(self):
        self.assertEqual(double_elements([1, 2, 3]), [2, 4, 6])

    def test_sum_elements(self):
        self.assertEqual(sum_elements([1, 2, 3]), 6)

if __name__ == "__main__":
    unittest.main()
