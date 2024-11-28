products = {0: "potatoes", 1: "tomatoes", 3: "onions", 4: "garlic"}
products2 = {7: "pepper", 8: "milk"}


def showDictionary(dictionary):
    """Print the dictionary with a pretty format"""
    for clave, valor in dictionary.items():
        print(f"Key: {clave}\n\tValue: {valor}")


def findValue(dictionary, key):
    """Find the value of a dict given the key and print it"""
    print(dictionary[key])


def mergeDictionaries(dictionaryA, dictionaryB):
    """Merge 2 dictionaries in one"""
    mergedDictionary = dictionaryA | dictionaryB

    return mergedDictionary


showDictionary(products)
products[5] = "eggs"
products[6] = "salt"
showDictionary(products)
findValue(products, 3)
showDictionary(mergeDictionaries(products, products2))
