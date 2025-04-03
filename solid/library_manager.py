from solid.library_interface import LibraryInterface
from solid.book import Book

# LibraryManager depends on abstraction (DIP)
class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title: str, author: str, year: str):
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title: str):
        self.library.remove_book(title)

    def show_books(self):
        books = self.library.get_all_books()
        if not books:
            print("Library is empty.")
        for book in books:
            print(book)
