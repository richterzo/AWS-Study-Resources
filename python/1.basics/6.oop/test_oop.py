import unittest
from oop import Car, ElectricCar, BankAccount


class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car("Toyota", "Camry", 2020)

    def test_car_accelerate(self):
        self.assertEqual(self.car.accelerate(), "2020 Toyota Camry is accelerating")

    def test_car_brake(self):
        self.assertEqual(self.car.brake(), "2020 Toyota Camry is braking")


class TestElectricCar(unittest.TestCase):
    def setUp(self):
        self.electric_car = ElectricCar("Tesla", "Model S", 2022, 100)

    def test_electric_car_accelerate(self):
        self.assertEqual(self.electric_car.accelerate(), "2022 Tesla Model S is accelerating rapidly")

    def test_electric_car_brake(self):
        self.assertEqual(self.electric_car.brake(), "2022 Tesla Model S is braking")

    def test_electric_car_battery(self):
        self.assertEqual(self.electric_car.describe_battery(), "The electric car's battery has a capacity of 100 kWh")


class TestPolymorphism(unittest.TestCase):
    def test_polymorphism(self):
        car = Car("Toyota", "Camry", 2020)
        electric_car = ElectricCar("Tesla", "Model S", 2022, 100)
        
        self.assertEqual(car.accelerate(), "2020 Toyota Camry is accelerating")
        self.assertEqual(electric_car.accelerate(), "2022 Tesla Model S is accelerating rapidly")


if __name__ == "__main__":
    unittest.main()


class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = Bank("Big Bank")

    def test_create_account(self):
        account = self.bank.create_account("Alice", 1000)
        self.assertEqual(account.owner, "Alice")
        self.assertEqual(account.balance, 1000)


if __name__ == "__main__":
    unittest.main()
