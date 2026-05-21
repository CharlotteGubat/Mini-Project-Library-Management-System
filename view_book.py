class Book:
    def __init__(self, book_id: str, title: str, author: str):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

class LibraryService:
    def __init__(self):
        self._books = {}
        
    def view_books(self):
        return list(self._books.values())


service = LibraryService()
choice = "5"

if choice == "5":
    books = service.view_books()
    if not books:
        print("Output: \"No books found.\"")
    else:
        print("Output: \"Books:\" header")
        for book in books:
            status = "Available" if book.available else "Borrowed"
            print(f"Output: \"[{book.book_id}] - {book.title} by {book.author} | ({status})\"")