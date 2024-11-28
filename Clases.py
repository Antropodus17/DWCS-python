from colorama import Fore
from datetime import date


class Person:
    """Class persona for managgin the data"""

    def __init__(self, name: str, email: str, telephone: str):
        self.name = name
        self.email = email
        self.telephone = telephone

    def __str__(self, tab=0) -> str:
        esp0 = "\n" + "\t" * tab
        esp1 = esp0 + "\t"
        return (
            Fore.BLUE
            + f"{esp0}Name: {self.name}{esp1}Email: {self.email}{esp1}Telephone: {self.telephone}"
            + Fore.RESET
        )


class Product:
    """Class product for managging the data"""

    def __init__(self, name: str, description: str, price: float, image: str):
        self.name = name
        self.description = description
        self.price = price
        self.image = image

    def __str__(self, tab=0) -> str:
        esp0 = "\n" + "\t" * tab
        esp1 = esp0 + "\t"
        return (
            Fore.MAGENTA
            + f"{esp0}Name: {self.name}{esp1}Description: {self.description}{esp1}Price: {self.price}{esp1}Image: {self.image}"
            + Fore.RESET
        )


class Order:
    """Class order for managging the data"""

    def __init__(self, date: date, products: list[Product], client: Person):
        self.date = date
        self.products = products
        self.client = client

    def getTotal(self) -> float:
        total = 0
        for product in self.products:
            total += product.price
        return total

    def __str__(self, tab=0) -> str:
        esp0 = "\n" + "\t" * tab

        cadena = Fore.GREEN + f"{esp0}Date: {self.date}"
        cadena += f"{esp0}Products:"
        for product in self.products:
            cadena += product.__str__(tab + 1)
        cadena += Fore.RED + f"{esp0}    Total Price: {self.getTotal()}"
        cadena += Fore.GREEN + f"{esp0}Person: "
        cadena += self.client.__str__(tab + 1)
        return cadena + Fore.RESET
