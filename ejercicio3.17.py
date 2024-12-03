from almacenClases import DivisionByZeroError
from colorama import Fore

continuar = True

# FUNCTIONS


def divide_numbers(numerator, denominator):
    if denominator == 0:
        raise DivisionByZeroError("Cannot divide by zero.")
    else:
        return numerator / denominator


while continuar:
    numerator = int(input(Fore.GREEN + "Introduce the Numerator: "))
    denominator = int(input("Introduce the Denominator: "))
    try:
        print(divide_numbers(numerator, denominator))
    except DivisionByZeroError as e:
        print(Fore.RED + e.__str__() + Fore.GREEN)
    finally:
        if (
            input(Fore.LIGHTBLUE_EX + "You want to make another divition?(y|N): ")
            != "y"
        ):
            continuar = False
