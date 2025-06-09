class Library:
    def __init__(self):
        self.db = []

    def add_book(self, book):
        self.db.append(book)
        print(f"Added book: {book.title}")

    def get_book_by_id(self, book_id):
        return next((b for b in self.db if b.book_id == book_id), None)

    def remove_book_by_id(self, book_id):
        book = self.get_book_by_id(book_id)
        if book:
            self.db.remove(book)
            print(f"Removed book: {book.title}")
        else:
            print("Book not found.")

    def update_book(self, book_id, title=None, description=None, add_authors=None, remove_author_indexes=None):
        book = self.get_book_by_id(book_id)
        if not book:
            return False, "Book not found."

        if title:
            book.title = title
        if description:
            book.description = description
        if add_authors:
            book.authors.extend(add_authors)
        if remove_author_indexes:
            try:
                for index in sorted(remove_author_indexes, reverse=True):
                    book.authors.pop(index)
            except IndexError:
                return False, "Invalid author index."

        return True, "Book updated."

    def search_by_title(self, keyword):
        return [b for b in self.db if keyword.lower() in b.title.lower()]

    def search_by_author(self, name):
        return [
            b for b in self.db
            if any(name.lower() in a.name.lower() for a in b.authors)
        ]

    def display_all_books(self):
        if not self.db:
            print("No books.")
        for book in self.db:
            print(book)
