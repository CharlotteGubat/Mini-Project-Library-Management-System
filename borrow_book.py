class Book:
    def __init__(self, book_id: str, title: str, author: str):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True
    def borrow(self):
        self.available = False

class Member:
    def __init__(self, member_id: str, name: str, email: str):
        self.member_id = member_id
        self.name = name
        self.email = email

class Loan:
    def __init__(self, loan_id: str, book: Book, member: Member):
        self.loan_id = loan_id
        self.book = book
        self.member = member


class BookNotFoundError(Exception): pass
class MemberNotFoundError(Exception): pass
class BookAlreadyBorrowedError(Exception): pass

class LibraryService:
    def __init__(self):
        self._books = {}
        self._members = {}
        self._loans = []

    def borrow_book(self, book_id: str, member_id: str):
        book = self._books.get(book_id)
        if book is None:
            raise BookNotFoundError("Book not found.")
        
        member = self._members.get(member_id)
        if member is None:
            raise MemberNotFoundError("Member not found.")
            
        if not book.available:
            raise BookAlreadyBorrowedError("Book is already borrowed.")
            
        book.borrow()
        loan_id = f"ln{len(self._loans) + 1:02d}" 
        new_loan = Loan(loan_id, book, member)
        self._loans.append(new_loan)
        return new_loan


service = LibraryService()
choice = "3"

if choice == "3":
    book_id = input("Input: Book ID: ")
    member_id = input("Input: Member ID: ")
    
    try:
        loan = service.borrow_book(book_id, member_id)
        print(f"Output: \"{loan.member.name} borrowed {loan.book.title}\"")
    except (BookNotFoundError, MemberNotFoundError, BookAlreadyBorrowedError) as e:
        print(f"Output: error message -> {e}")