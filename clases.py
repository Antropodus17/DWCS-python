class Dog:

    def bark():
        print("BARK")


my_dog = Dog()
my_dog.name = "Hola"
Dog.name = "Adios"
print(my_dog.name)
