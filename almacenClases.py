"""docstring for Car."""


class Car:
    """Constructor"""

    def __init__(self, color, power):
        self.color = color
        self.power = power

    def __str__(self):
        return f"This car is :self.color and have :self.power horse"


"""Class Calculator for make calculations"""


class Calculator:

    numberOfObjects = 0

    def __init__(self, num1=0, num2=0):
        self.setNum1(num1)
        self.setNum2(num2)
        Calculator.numberOfObjects += 1

    """Setter for the num1"""

    def setNum1(self, num):
        if type(num) != int:
            raise TypeError("The number must be a integer")

        self.num1 = num

    """Getter of the num2"""

    def getNumb1(self):
        return self.num1

    """Setter for the num2"""

    def setNum2(self, num):
        if type(num) != int:
            raise TypeError("The number must be a integer")

        self.num2 = num

    """Getter of the num2"""

    def getNumb2(self):
        return self.num2

    """To string of the Calculator"""

    def __str__(self):
        return f"Numero 1: {self.num1}\nNumero 2: {self.num2}\nSuma: {self.sum()}"

    """Method to return the sum of the two nums"""

    def sum(self):
        return self.num1 + self.num2
