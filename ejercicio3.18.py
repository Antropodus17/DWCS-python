from Clases import *

i = 0
books = []
while i < 10:
    estado = True if i % 2 == 0 else False
    books.append(Book(f"Book {i}", f"author {i}", estado))
    i += 1

libreria = Library(books)
libreria.listAvaliableBooks()
