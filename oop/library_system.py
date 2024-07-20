class Book:

    def __init__ (self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Title {self.title}, and author {self.author}"
    
class EBook(Book):
    def __init__ (self, title, author, file_size):
        super().__init__(self, title, author)
        self.file_size = file_size 

    def __str__(self):
        return f"{Book.title} {Book.author} size {self.file_size}"

class PrintBook(Book):
    def __init__ (self, title, author, page_count):
        super().__init__(self, author, title)
        self.page_count = page_count

    def __Str__(self):
        return f"{Book.title} {Book.author} page count {self.page_count}"

class Library:
    def __init__(self, books):
        self.books = books
        self.add_book = []

    def add_book (self, book):
        self.add_book.append(book)

    def list_books (self):
        return f"list of books: {Library.add_book}"