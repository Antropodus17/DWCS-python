"""docstring for Car."""


class Car:
    """Constructor"""

    def __init__(self, color, power):
        self.color = color
        self.power = power

    def __str__(self):
        return f"This car is :self.color and have :self.power horse"


"""Class Calculator for make calculations"""


class Calculator:

    numberOfObjects = 0

    def __init__(self, num1=0, num2=0):
        self.setNum1(num1)
        self.setNum2(num2)
        Calculator.numberOfObjects += 1

    """Setter for the num1"""

    def setNum1(self, num):
        if type(num) != int:
            raise TypeError("The number must be a integer")

        self.num1 = num

    """Getter of the num2"""

    def getNumb1(self):
        return self.num1

    """Setter for the num2"""

    def setNum2(self, num):
        if type(num) != int:
            raise TypeError("The number must be a integer")

        self.num2 = num

    """Getter of the num2"""

    def getNumb2(self):
        return self.num2

    """To string of the Calculator"""

    def __str__(self):
        return f"Numero 1: {self.num1}\nNumero 2: {self.num2}\nSuma: {self.sum()}"

    """Method to return the sum of the two nums"""

    def sum(self):
        return self.num1 + self.num2


# ejercicio 3.7
"""Persona"""


class Person:
    """Constructor"""

    def __init__(self, id, name, age):
        self.setId(id)
        self.setName(name)
        self.setAge(age)

    """SETTERS"""

    def setId(self, id):
        self.id = str(id)

    def setName(self, name):
        self.name = str(name)

    def setAge(self, age):
        self.age = int(age)

    """TO STRING"""

    def __str__(self, tab=0):
        return f"{'    '*tab}Id: {self.id}\n{'    '*tab}Name: {self.name}\n{'    '*tab}Age: {self.age}"


"""Estudiante"""


class Student:

    def __init__(self, id, degree, person):
        self.setId(id)
        self.setDegree(degree)
        self.setPerson(person)

    def setId(self, id):
        self.id = str(id)

    def setDegree(self, degree):
        self.degree = str(degree)

    def setPerson(self, person):
        if type(person) == Person:
            self.person = person
        else:
            raise TypeError("Person must be of type Person")

    def __str__(self, tab=0):
        return f"{'    '*tab}Id: {self.id}\n{'    '*tab}Degree: {self.degree}\n{'    '*tab}Person:\n{self.person.__str__(tab+1)}"


"""Grupo de estudiantes"""


class StudentGroup:
    """Constructor"""

    def __init__(self, id, name, students):
        self.setId(id)
        self.setName(name)
        self.setStudents(students)

    """SETTERS"""

    def setId(self, id):
        self.id = str(id)

    def setName(self, name):
        self.name = str(name)

    def setStudents(self, students):
        self.students = []
        for student in students:
            if type(student) == Student:
                self.students.append(student)

    """TO STRING"""

    def __str__(self, tab=0) -> str:
        std = "" if self.students == [] else "Students: "
        return f"{'    '*tab}Id: {self.id}\n{'    '*tab}Name: {self.name}\n{'    '*tab}{std}{self.stringStudents(tab)}"

    def stringStudents(self, tab):
        studentsString = ""
        for student in self.students:
            studentsString += f"\n{student.__str__(tab+1)}"
        return studentsString


class Alien:
    """Alien class"""

    numberOfAlien = 0

    def __init__(self, name):
        self.name = name
        Alien.numberOfAlien += 1

    @staticmethod
    def getNumberOfAliens():
        return Alien.numberOfAlien
