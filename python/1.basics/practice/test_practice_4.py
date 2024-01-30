import unittest
from practice_4 import Circle, Rectangle, BankAccount, Employee, Triangle

class TestOOPChallenges(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(5, "red")
        self.assertAlmostEqual(circle.calculate_area(), 78.54, places=2)

    def test_rectangle_perimeter(self):
        rectangle = Rectangle(3, 4)
        self.assertEqual(rectangle.calculate_perimeter(), 14)

    def test_bank_account_deposit(self):
        account = BankAccount("123456", 1000, "John Doe")
        account.deposit(500)
        self.assertEqual(account.balance, 1500)

    def test_employee_bonus(self):
        employee = Employee("Alice", "Manager", 50000)
        self.assertEqual(employee.calculate_bonus(), 2500)

    def test_triangle_equilateral(self):
        triangle = Triangle(5, 5, 5)
        self.assertTrue(triangle.is_equilateral())

if __name__ == "__main__":
    unittest.main()
