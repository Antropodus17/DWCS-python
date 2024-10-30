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
        return f"{"\t"*tab}Id: {self.id}\n{"\t"*tab}Name: {self.name}\n{"\t"*tab}Age: {self.age}"


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
        return f"{"\t"*tab}Id: {self.id}\n{"\t"*tab}Degree: {self.degree}\n{"\t"*tab}Person: {self.person}"
    

"""Grupo de estudiantes"""
class studentGroup:

    """Constructor"""
    def __init__(self, id,name ,students):
        self.setId(id)

    """SETTERS"""
    def setId(self,id):
        self.id=str(id)

    def setName(self,name):
        self.name=str(name)

    def setStudents(self,students):
        self.students=[]
        for student in students:
            if type(student)==Student:
                self.students.append(student)
    """TO STRING"""
    def __str__(self) -> str:
        pass
    