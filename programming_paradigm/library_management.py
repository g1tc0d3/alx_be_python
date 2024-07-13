class Book:
    def __init__ (self, title, author, _is_checked_out):
        self.title = title
        self.author = author
        self._is_checked_out = _is_checked_out
        pass
    
class Library:
    def __init__(self, _books, add_book, check_out_book, return_book, list_available_books):
        self._books = _books
        self.add_book = Book.append()
        self.check_out_book = check_out_book
        self.return_book = return_book
        self.list_availbale_book = Book.list()

        


