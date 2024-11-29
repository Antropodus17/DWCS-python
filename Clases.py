from colorama import Fore
from typing import Self


class Book:
    """Class for managging book data."""

    def __init__(self: Self, name: str, autor: str, status: bool) -> Self:

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
        print(self.books)
        map(print, map(lambda o: o if o.status else None, self.books))
