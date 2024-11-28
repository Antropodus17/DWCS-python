from Clases import Person, Student, StudentGroup


student1 = Student(1, "Algebra", Person(1, "Sergio", 22))
student2 = Student(2, "Dibujo", Person(1, "Jóse", 20))
student3 = Student(3, "Logica", Person(1, "Dani", 23))

print(student1)
print(student2)
print(student3)

grupo = StudentGroup("G-1", "Prueba Grupo", [student1, student2, student3])

print("\n\nGrupo\n\n")
print(grupo)


print("\n\nGrupo Vacio\n\n")
grupo.setStudents([])
print(grupo)


print("\n\nGrupo 1 integrante\n\n")
grupo.setStudents([Student(4, "ingenieria", Person(4, "Alicia", 25))])
print(grupo)
