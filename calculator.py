from Clases import Calculator

try:
    print("***FIRST CALCULE***")
    first_calcule = Calculator()
    first_calcule.setNum1(5)
    first_calcule.setNum2(6)
    print(f"Number 1: {first_calcule.getNumb1()}")
    print(f"Number 2: {first_calcule.getNumb2()}")

    print("***SECOND CALCULE***")
    second_calcule = Calculator()
    second_calcule = Calculator(8, 9)
    print(second_calcule)

    print("***SUMS***")
    print(first_calcule.sum())
    print(second_calcule.sum())

except Exception as e:
    print(e)
