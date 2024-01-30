import unittest
from practice_3 import *


class TestChallenges(unittest.TestCase):
    def test_find_max(self):
        self.assertEqual(find_max(5, 10), 10)
        self.assertEqual(find_max(100, 20), 100)
        self.assertEqual(find_max(-5, -10), -5)

    def test_reverse_list(self):
        self.assertEqual(reverse_list([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse_list(['a', 'b', 'c']), ['c', 'b', 'a'])
        self.assertEqual(reverse_list([]), [])

    def test_sum_list(self):
        self.assertEqual(sum_list([1, 2, 3]), 6)
        self.assertEqual(sum_list([10, 20, 30]), 60)
        self.assertEqual(sum_list([-1, 0, 1]), 0)

    def test_divide_numbers(self):
        self.assertEqual(divide_numbers(10, 2), 5)
        self.assertEqual(divide_numbers(100, 10), 10)
        self.assertEqual(divide_numbers(5, 0), "Division by zero is not allowed")

    def test_search_element(self):
        self.assertEqual(search_element([1, 2, 3, 4, 5], 3), "Element found at index 2")
        self.assertEqual(search_element(['a', 'b', 'c'], 'd'), "Element not found in the list")

    def test_is_list_empty(self):
        self.assertTrue(is_list_empty([]))
        self.assertFalse(is_list_empty([1, 2, 3]))

    def test_merge_lists(self):
        self.assertEqual(merge_lists([1, 2], [3, 4]), [1, 2, 3, 4])
        self.assertEqual(merge_lists(['a'], ['b']), ['a', 'b'])

    def test_count_occurrences(self):
        self.assertEqual(count_occurrences([1, 2, 2, 3, 3, 3], 2), 2)
        self.assertEqual(count_occurrences(['a', 'b', 'c', 'c'], 'c'), 2)

    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 3, 3]), [1, 2, 3])
        self.assertEqual(remove_duplicates(['a', 'b', 'b', 'c', 'c']), ['a', 'b', 'c'])

    def test_generate_even_numbers(self):
        self.assertEqual(generate_even_numbers(5), [0, 2, 4])
        self.assertEqual(generate_even_numbers(10), [0, 2, 4, 6, 8, 10])


if __name__ == '__main__':
    unittest.main()
