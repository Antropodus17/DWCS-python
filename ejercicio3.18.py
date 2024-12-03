from Clases import Book, Library, BookNotAvailableException, BookNotFoundException

i = 0
books = []
while i < 10:
    estado = True if i % 2 == 0 else False
    books.append(Book(f"Book {i}", f"author {i}", estado))
    i += 1
books.append(Book("Berserk", "Kentaro Miura", True))
libreria = Library(books)

seguirMenu = True

while seguirMenu:
    menu = """Welcome to Library Baroja:
    1) List Books:
    2) Borrow Book:
    3) Return Book:
    4) Exit:
    Option: """
    opcion = input(menu)
    try:
        match opcion:
            case "1":
                libreria.listAvaliableBooks()

            case "2":
                libreria.borrowBook(input("Inroduce th title of the book: "))

            case "3":
                libreria.returnBook(input("Introduce the title of the book: "))

            case "4":
                seguirMenu = False
                print("Good bye")

            case _:
                print("Not valid option")
    except BookNotFoundException as e:
        print(e)
    except BookNotAvailableException as e:
        print(e)
