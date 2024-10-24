def presentation(age, name=None, surname="Apelido"):
    print(("" if (name == None) else str(name)) + f"{surname} is {age} years old")


presentation(22)
