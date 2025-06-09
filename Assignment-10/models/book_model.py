class Book:
    book_count = 0

    @staticmethod
    def get_new_book_id():
        Book.book_count += 1
        return Book.book_count

    def __init__(self, title, authors, sbn_number, description):
        self.book_id = Book.get_new_book_id()
        self.title = title
        self.authors = authors
        self.sbn_number = sbn_number
        self.description = description

    def __repr__(self):
        authors_str = ", ".join([a.name for a in self.authors])
        return f"[{self.book_id}] '{self.title}' by {authors_str}"
