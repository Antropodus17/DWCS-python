# Write a function called "potencia".
# It receives two integer numbers. Check that the numbers are integer. If they are not, raise an exception.
# It calculates the power using a loop and returns the result.
# Write a program that invokes the previous function. Use exceptions.
def potencia(base: int, power: int) -> int:
    total = 1
    print(f"Base: {base}:{type(base)}")
    print(f"Power: {power}:{type(power)}")
    if type(base) == type(power) == int:
        for i in range(power):
            total *= base
    else:
        raise TypeError("La base y la potencia tienen que ser de tipo entero")
    return total


try:
    print(potencia(5, 3))
except Exception as e:
    print(e)
