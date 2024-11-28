# Function factorial

# Write a function that receives an integer number and returns its factorial.

# It performs the following tasks:

#     Check that it is an integer equal or greater than 0.
#     If it doesn't pass the previous check it must raise an exception with the information of the error.
#     If everything is ok it uses a loop to calculate the factorial and it returns it.

# Program

# Write the code that invokes the previous function and shows the result.

# Include exception handling and show the messages on the screen.


def factorial(base):
    if type(base) != int:
        raise TypeError("It must be an Integer number")
    if base < 0:
        raise TypeError("The number must equal or greatter than Zero")
    result = 1
    for i in range(base, 0, -1):
        result *= i

    return result


try:
    print(factorial(5))
except TypeError as e:
    print(e)
