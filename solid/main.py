from solid.library import Library
from solid.library_manager import LibraryManager

def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                year = input("Enter book year: ")
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ")
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
