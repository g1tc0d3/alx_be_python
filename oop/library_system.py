class Book:

    def __init__ (self, title, author):
        self.title = title
        self.author = author

class EBook (Book):
    def __init__ (self, title, author, file_size):
        Book.__init__(self, title, author)
        self.file_size = file_size 

class PrintBook (Book):
    def __init__ (self, title, author, page_count):
        Book.__init__(self, author, title)
        self.page_count = page_count

class Library:
    def __init__(self, books):
        self.books = books
        self.add_book = []

    def add_book (self, book):
        self.add_book.append(book)

    def list_books (self):
        return f"list of books: {Library.add_book}"