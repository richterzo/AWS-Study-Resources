import unittest
from practice_2 import count_vowels, is_palindrome, even_numbers, fizzbuzz, factorial, is_anagram, sum_odd_numbers, is_prime, power, is_pangram


class TestChallenges(unittest.TestCase):
    def test_count_vowels(self):
        self.assertEqual(count_vowels("Hello World"), 3)
        self.assertEqual(count_vowels("Python"), 1)
        self.assertEqual(count_vowels("AEIOUaeiou"), 10)

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("radar"))
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("python"))

    def test_even_numbers(self):
        even_numbers_list = even_numbers()
        self.assertEqual(even_numbers_list, [2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(), [
            1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz',
            16, 17, 'Fizz', 19, 'Buzz'
        ])

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)

    def test_anagram(self):
        self.assertTrue(is_anagram('listen', 'silent'))
        self.assertFalse(is_anagram('hello', 'world'))

    def test_sum_odd_numbers(self):
        self.assertEqual(sum_odd_numbers(), 2500)

    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(7))
        self.assertFalse(is_prime(10))
        self.assertFalse(is_prime(1))

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(3, 4), 81)

    def test_is_pangram(self):
        self.assertTrue(is_pangram('The quick brown fox jumps over the lazy dog'))
        self.assertFalse(is_pangram('Hello world'))

if __name__ == '__main__':
    unittest.main()
