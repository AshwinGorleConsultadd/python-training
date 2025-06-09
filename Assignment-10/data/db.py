class Author() :
    name : str

class Book() :
    book_count = 0;
    @staticmethod
    def get_new_book_id () :
        Book.book_count += 1
        return Book.book_count
    def __init__ (self, title, author, sbn_number, description) :
        self.title = title
        self.author = author
        self.sbn_number = sbn_number
        self.description = description





