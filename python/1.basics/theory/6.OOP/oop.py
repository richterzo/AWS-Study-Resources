# Definizione della classe Car
class Car:
    """
    Classe che rappresenta un'auto.
    """

    def __init__(self, make, model, year):
        """
        Inizializza gli attributi dell'auto.

        Args:
            make (str): La marca dell'auto.
            model (str): Il modello dell'auto.
            year (int): L'anno di produzione dell'auto.
        """
        self.make = make
        self.model = model
        self.year = year

    def accelerate(self):
        """
        Simula l'accelerazione dell'auto.

        Returns:
            str: La stringa che rappresenta l'accelerazione dell'auto.
        """
        return f"{self.year} {self.make} {self.model} is accelerating"

    def brake(self):
        """
        Simula il freno dell'auto.

        Returns:
            str: La stringa che rappresenta il freno dell'auto.
        """
        return f"{self.year} {self.make} {self.model} is braking"


# Definizione della classe ElectricCar
class ElectricCar(Car):
    """
    Classe che rappresenta un'auto elettrica, ereditata dalla classe Car.
    """

    def __init__(self, make, model, year, battery_capacity):
        """
        Inizializza gli attributi dell'auto elettrica.

        Args:
            make (str): La marca dell'auto.
            model (str): Il modello dell'auto.
            year (int): L'anno di produzione dell'auto.
            battery_capacity (float): La capacità della batteria dell'auto elettrica.
        """
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity

    def describe_battery(self):
        """
        Descrive la capacità della batteria dell'auto elettrica.

        Returns:
            str: La stringa che descrive la capacità della batteria dell'auto elettrica.
        """
        return f"The electric car's battery has a capacity of {self.battery_capacity} kWh"

    def accelerate(self):
        return f"{self.year} {self.make} {self.model} is accelerating rapidly"

# Definizione della classe BankAccount
class BankAccount:
    """
    Classe che rappresenta un conto bancario.
    """

    def __init__(self, account_number, balance):
        """
        Inizializza gli attributi del conto bancario.

        Args:
            account_number (str): Il numero del conto bancario.
            balance (float): Il saldo del conto bancario.
        """
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        """
        Deposita una certa quantità sul conto.

        Args:
            amount (float): La quantità da depositare.
        """
        self.balance += amount

    def withdraw(self, amount):
        """
        Preleva una certa quantità dal conto, se possibile.

        Args:
            amount (float): La quantità da prelevare.
        """
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        """
        Ottiene il saldo attuale del conto.

        Returns:
            float: Il saldo attuale del conto.
        """
        return self.balance
