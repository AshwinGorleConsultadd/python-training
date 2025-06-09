from services.library import Library
from models.book_model import Book
from models.author_model import Author

class LibraryCLI:
    def __init__(self):
        self.library = Library()

    def run(self):
        while True:
            self.display_menu()
            choice = input("Choose an option: ")
            self.handle_choice(choice)

    def display_menu(self):
        print("\n=== Library Management CLI ===")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Edit Book")
        print("4. Delete Book")
        print("5. Search Books")
        print("6. Exit")

    def handle_choice(self, choice):
        match choice:
            case '1': self.add_book()
            case '2': self.library.display_all_books()
            case '3': self.edit_book()
            case '4': self.delete_book()
            case '5': self.search_books()
            case '6': exit("Goodbye!")
            case _: print("Invalid choice.")

    def input_authors(self):
        authors = []
        while True:
            name = input("Enter author name (or press Enter to stop): ").strip()
            if not name:
                break
            authors.append(Author(name))
        return authors

    def add_book(self):
        title = input("Enter title: ")
        sbn = input("Enter SBN: ")
        desc = input("Enter description: ")
        authors = self.input_authors()
        book = Book(title, authors, sbn, desc)
        self.library.add_book(book)

    def edit_book(self):
        try:
            book_id = int(input("Book ID to edit: "))
        except ValueError:
            print("Invalid ID.");
            return

        book = self.library.get_book_by_id(book_id)
        if not book:
            print("Book not found.");
            return

        print("1. Change Title\n2. Change Description\n3. Add Author\n4. Remove Author")
        choice = input("Choose option: ")

        if choice == '1':
            new_title = input("New Title: ")
            success, msg = self.library.update_book(book_id, title=new_title)

        elif choice == '2':
            new_desc = input("New Description: ")
            success, msg = self.library.update_book(book_id, description=new_desc)

        elif choice == '3':
            new_authors = self.input_authors()
            success, msg = self.library.update_book(book_id, add_authors=new_authors)

        elif choice == '4':
            if not book.authors:
                print("No authors to remove.");
                return
            for i, a in enumerate(book.authors): print(f"{i + 1}. {a.name}")
            try:
                idx = int(input("Author # to remove: ")) - 1
                success, msg = self.library.update_book(book_id, remove_author_indexes=[idx])
            except ValueError:
                print("Invalid input.");
                return

        else:
            print("Invalid option.")
            return

        print(msg if success else f"Error: {msg}")

    def delete_book(self):
        try:
            book_id = int(input("Book ID to delete: "))
        except ValueError:
            print("Invalid ID."); return

        book = self.library.get_book_by_id(book_id)
        if not book:
            print("Book not found."); return

        confirm = input(f"Delete '{book.title}'? (y/n): ").lower()
        if confirm == 'y':
            self.library.remove_book_by_id(book_id)
        else:
            print("Deletion cancelled.")

    def search_books(self):
        print("1. By Title\n2. By Author")
        choice = input("Choose: ")
        keyword = input("Enter keyword: ")

        if choice == '1':
            results = self.library.search_by_title(keyword)
        elif choice == '2':
            results = self.library.search_by_author(keyword)
        else:
            print("Invalid choice."); return

        if results:
            for book in results: print(book)
        else:
            print("No results.")
