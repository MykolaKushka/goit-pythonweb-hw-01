from abc import ABC, abstractmethod
from solid.book import Book

# Interface for Library operations
class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book):
        pass

    @abstractmethod
    def remove_book(self, title: str):
        pass

    @abstractmethod
    def get_all_books(self) -> list[Book]:
        pass
