from solid.library_interface import LibraryInterface
from solid.book import Book

# Concrete implementation of LibraryInterface
class Library(LibraryInterface):
    def __init__(self):
        self.books: list[Book] = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, title: str):
        self.books = [book for book in self.books if book.title != title]

    def get_all_books(self) -> list[Book]:
        return self.books
