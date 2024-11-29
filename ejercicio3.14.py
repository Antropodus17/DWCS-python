products = {0: "potatoes", 1: "tomatoes", 3: "onions", 4: "garlic"}
products2 = {7: "pepper", 8: "milk"}
import operator


def showDictionary(dictionary):
    """Print the dictionary with a pretty format"""
    for clave, valor in dictionary.items():
        print(f"Key: {clave}\n\tValue: {valor}")


def findValue(dictionary: dict, key: str):
    """Find the value of a dict given the key and print it"""
    if key in dictionary.keys():
        print(dictionary[key])
    else:
        print(f"No existe la clave: {key}")


def mergeDictionaries(dictionaryA, dictionaryB):
    """Merge 2 dictionaries in one"""
    mergedDictionary = dictionaryA | dictionaryB
    operator.or_(dictionaryA, dictionaryB)

    return mergedDictionary


showDictionary(products)
products[5] = "eggs"
products[6] = "salt"
showDictionary(products)
findValue(products, 3)
showDictionary(mergeDictionaries(products, products2))
