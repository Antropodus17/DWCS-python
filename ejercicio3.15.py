import json, builtins
from colorama import Fore, Back

# FUNCTIONS


def showDictionary(dictionary: dict, tab: int = 0) -> None:
    color = Fore.BLUE
    esp = "\t"
    for k, v in dictionary.items():
        match type(v):
            case builtins.dict:
                print(f"{color+esp*tab}{k}:")
                showDictionary(v, tab + 1)
                break
            case builtins.list:
                print(f"{color+esp*tab}{k}:")
                for value in v:
                    showDictionary(value, tab + 1)
            case default:

                print(f"{color+esp*tab}{k}: {v}")


def makeListField(lista: list, field: str) -> list:
    """create a list of fields of dictionaries"""
    resultado = []
    for book in lista:
        resultado.append(book[field])
    return resultado


def findValue(dictionary: dict, id: int) -> dict | None:
    """Find the book that conatins the id or None if not found"""
    books = dictionary["catalog"]["book"]
    for book in books:
        if book["id"] == id:
            return book

    return None


# LOAD OF THE CATALOG.JSON
with open("catalog.json") as f:
    catalog = json.load(f)


# PROGRAM
print(Fore.GREEN + "*********SHOW THE CATALOG**********")
showDictionary(catalog)
input(Fore.RED + "Press enter to Continue")
print(Fore.GREEN + "*********SHOW THE TITLES**********")
print(Fore.LIGHTMAGENTA_EX + f'{makeListField(catalog["catalog"]["book"], "title")}')
input(Fore.RED + "Press enter to Continue")
print(Fore.GREEN + "*********SHOW THE BOOK WITH INDEX X(5)**********")
showDictionary(findValue(catalog, 5))
