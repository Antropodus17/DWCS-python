# 1. tripleCheck

# This function receives a list of integers and returns a boolean indicating if a triple is present in that array or not. If a value appears three times in a row in an array it is called a triple.

# Sample Input:
# { 1, 1, 2, 2, 1 }
# { 1, 1, 2, 1, 2, 3 }
# { 1, 1, 1, 2, 2, 2, 1 }
# Sample Output:
# bool(false)
# bool(false)
# bool(true)


def tripleCheck(lista):
    if type(lista) != list:
        raise TypeError("It must be a list")
    for index in range(0, len(lista) - 2):
        if lista[index] == lista[index + 1] == lista[index + 2]:
            return True

    return False


print(tripleCheck([1, 1, 2, 2, 1]))
print(tripleCheck([1, 1, 2, 1, 2, 3]))
print(tripleCheck([1, 1, 1, 2, 2, 2, 1]))
print(tripleCheck([0, 1, 1, 1]))


# 2. countries

# This function receives a list with pairs country - capital and shows a description on the screen as below:

ceu = {
    "Italy": "Rome",
    "Luxembourg": "Luxembourg",
    "Belgium": "Brussels",
    "Denmark": "Copenhagen",
    "Finland": "Helsinki",
    "France": "Paris",
    "Slovakia": "Bratislava",
    "Slovenia": "Ljubljana",
    "Germany": "Berlin",
    "Greece": "Athens",
    "Ireland": "Dublin",
    "Netherlands": "Amsterdam",
    "Portugal": "Lisbon",
    "Spain": "Madrid",
    "Sweden": "Stockholm",
    "United Kingdom": "London",
    "Cyprus": "Nicosia",
    "Lithuania": "Vilnius",
    "Czech Republic": "Prague",
    "Estonia": "Tallin",
    "Hungary": "Budapest",
    "Latvia": "Riga",
    "Malta": "Valetta",
    "Austria": "Vienna",
    "Poland": "Warsaw",
}

# Sample Output :

# The capital of Netherlands is Amsterdam
# The capital of Greece is Athens
# The capital of Germany is Berlin


def capitalize(dictionarie: list):
    for country, capital in dictionarie.items():
        print(f"The capital of {country} is {capital}")


capitalize(ceu)
