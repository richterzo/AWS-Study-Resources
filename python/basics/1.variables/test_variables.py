import unittest
from variables import *

class TestVariables(unittest.TestCase):
    def test_integer_variable(self):
        self.assertEqual(type(x), str)
    
    def test_float_variable(self):
        self.assertEqual(type(y), float)
    
    def test_string_variable(self):
        self.assertEqual(type(name), str)
    
    def test_boolean_variable(self):
        self.assertEqual(type(is_true), bool)
    
    def test_size_of_variables(self):
        # Verifica che le dimensioni siano inferiori ai valori attesi
        self.assertLessEqual(sys.getsizeof(x), 54)  # Valore di esempio, adatta secondo le tue necessità
        self.assertLessEqual(sys.getsizeof(y), 32)  # Valore di esempio, adatta secondo le tue necessità
        self.assertLessEqual(sys.getsizeof(name), 64)  # Valore di esempio, adatta secondo le tue necessità
        self.assertLessEqual(sys.getsizeof(is_true), 32)  # Valore di esempio, adatta secondo le tue necessità

if __name__ == '__main__':
    unittest.main()
