import unittest
from functions import greet, greet_user, add_numbers, greet_user_default, greet_users, describe_pet

class TestFunctions(unittest.TestCase):
    """
    Test per le funzioni definite in functions.py
    """

    def test_greet(self):
        """
        Test per la funzione greet()
        """
        expected_output = "Ciao! Benvenuto!"
        self.assertEqual(greet(), expected_output)

    def test_greet_user(self):
        """
        Test per la funzione greet_user()
        """
        expected_output = "Ciao, Alice! Benvenuto!"
        self.assertEqual(greet_user("Alice"), expected_output)

    def test_add_numbers(self):
        """
        Test per la funzione add_numbers()
        """
        self.assertEqual(add_numbers(3, 5), 8)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)

    def test_greet_user_default(self):
        """
        Test per la funzione greet_user_default()
        """
        expected_output_default = "Ciao, Guest! Benvenuto!"
        expected_output_custom = "Ciao, Bob! Benvenuto!"
        self.assertEqual(greet_user_default(), expected_output_default)
        self.assertEqual(greet_user_default("Bob"), expected_output_custom)

    def test_greet_users(self):
        """
        Test per la funzione greet_users()
        """
        expected_output = "Ciao, Alice! Benvenuto!\nCiao, Bob! Benvenuto!\nCiao, Charlie! Benvenuto!"
        self.assertEqual(greet_users("Alice", "Bob", "Charlie"), expected_output)

    def test_describe_pet(self):
        """
        Test per la funzione describe_pet()
        """
        expected_output_cane = "Il mio cane si chiama Fido."
        expected_output_gatto = "Il mio gatto si chiama Whiskers."
        self.assertEqual(describe_pet("Fido"), expected_output_cane)
        self.assertEqual(describe_pet("Whiskers", animal_type="gatto"), expected_output_gatto)

if __name__ == '__main__':
    unittest.main()
