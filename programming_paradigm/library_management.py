class Book:
    def __init__(self, title, author, _is_checked_out,):
        self.title = title
        self.author = author
        self._is_checked_out = _is_checked_out



        pass
    
class Library:
    def __init__(self, add_book, checkout_book, return_book, list_available_books):
        self.add_book = Book.append()
        self.checkout_book = checkout_book
        self.return_book = return_book
        self.list_available_books = list_available_books
        pass