class Author:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"Author(name='{self.name}')"


class Book:
    book_count = 0

    @staticmethod
    def get_new_book_id():
        Book.book_count += 1
        return Book.book_count

    def __init__(self, title: str, authors: list, sbn_number: str, description: str):
        self.book_id = Book.get_new_book_id()
        self.title = title
        self.authors = authors          # This is a list of Author objects
        self.sbn_number = sbn_number
        self.description = description

    def __repr__(self):
        author_names = ', '.join([a.name for a in self.authors])
        return (f"Book(id={self.book_id}, title='{self.title}', "
                f"authors=[{author_names}], sbn_number='{self.sbn_number}')")
