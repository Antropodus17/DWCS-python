from colorama import Fore


class BookNotAvailableException(Exception):
    pass


class BookNotFoundException(Exception):
    pass


class Book:
    """Class for managging book data."""

    def __init__(self, name: str, autor: str, status: bool):

        self.name = name
        self.autor = autor
        self.status = status

    def __str__(self):
        return f"{self.name}"


class Library:
    """docstring for Library."""

    def __init__(self, books: list[Book]):
        self.books = books

    def listAvaliableBooks(self):
        libros_disponibles = map(lambda o: o if o.status else None, self.books)

        for book in libros_disponibles:
            if book != None:
                print(book)

    def borrowBook(
        self, title: str
    ) -> Book | BookNotFoundException | BookNotAvailableException:
        for book in self.books:
            if book.name == title:
                if book.status:
                    print(f"Book {title} borrowed")
                    book.status = False
                    return book
                else:
                    raise BookNotAvailableException(f"Book {title} not avaliable")
        raise BookNotFoundException(f"Book {title} not found.")

    def returnBook(self, title: str):
        for book in self.books:
            if book.name == title:
                if not book.status:
                    print(f"Book {title} returned")
                    book.status = True
                    return book
                else:
                    raise BookNotFoundException(f"Book {title} is not borrowed. ")
        raise BookNotFoundException(f"We don`t accept donations")
