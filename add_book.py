class Book:
    def __init__(self, book_id: str, title: str, author: str):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True
        
class LibraryService:
    def __init__(self):
        self._books = {}

    def add_book(self, book_id: str, title: str, author: str):
        new_book = Book(book_id, title, author)
        self._books[book_id] = new_book
        return new_book

service = LibraryService()

choice = "1"

if choice == "1":
    book_id = input("Input: Book ID: ")
    title = input("Input: Book Title: ")
    author = input("Input: Book Author: ")
    
    book = service.add_book(book_id, title, author)
    print(f"Output: \"Book added: {book.title}\"")