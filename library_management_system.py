import sys

# ==========================================
# DATA MODELS
# ==========================================

class Book:
    def __init__(self, book_id: str, title: str, author: str):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        self.available = False

    def return_book(self):
        self.available = True


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
        self.is_active = True


# ==========================================
# CUSTOM EXCEPTIONS (For Flowchart 3 & 4)
# ==========================================

class BookNotFoundError(Exception): pass
class MemberNotFoundError(Exception): pass
class BookAlreadyBorrowedError(Exception): pass
class LoanNotFoundError(Exception): pass


# ==========================================
# LIBRARY SERVICE (Storage & Processing)
# ==========================================

class LibraryService:
    def __init__(self):
        self._books = {}
        self._members = {}
        self._loans = []


    def add_book(self, book_id: str, title: str, author: str):
        new_book = Book(book_id, title, author)
        self._books[book_id] = new_book
        return new_book


    def register_member(self, member_id: str, name: str, email: str):
        new_member = Member(member_id, name, email)
        self._members[member_id] = new_member
        return new_member

 
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

  
    def return_book(self, book_id: str):
        book = self._books.get(book_id)
        if book is None:
            raise BookNotFoundError("Book not found.")
            
        active_loan = None
        for loan in self._loans:
            if loan.book.book_id == book_id and loan.is_active:
                active_loan = loan
                break
                
        if active_loan is None:
            raise LoanNotFoundError("No active loan found for this book.")
            
        book.return_book()
        active_loan.is_active = False
        return active_loan


    def view_books(self):
        return list(self._books.values())

 
    def view_members(self):
        return list(self._members.values())

   
    def view_loans(self):
        return self._loans


# ==========================================
# MAIN INTERFACE RUNTIME LOOP
# ==========================================

def main():
    service = LibraryService()
    
    while True:
        print("\n=== Library Management Menu ===")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View Books")
        print("6. View Members")
        print("7. View Loans")
        print("8. Exit")
        
        choice = input("Enter choice (1-8): ").strip()
        print("-" * 35)

  
        if choice == "1":
            book_id = input("Input: Book ID: ")
            title = input("Input: Book Title: ")
            author = input("Input: Book Author: ")
            
            book = service.add_book(book_id, title, author)
            print(f"Output: \"Book added: {book.title}\"")

   
        elif choice == "2":
            member_id = input("Input: Member ID: ")
            name = input("Input: Member Name: ")
            email = input("Input: Member Email: ")
            
            member = service.register_member(member_id, name, email)
            print(f"Output: \"Member registered: {member.name}\"")

   
        elif choice == "3":
            book_id = input("Input: Book ID: ")
            member_id = input("Input: Member ID: ")
            
            try:
                loan = service.borrow_book(book_id, member_id)
                print(f"Output: \"{loan.member.name} borrowed {loan.book.title}\"")
            except (BookNotFoundError, MemberNotFoundError, BookAlreadyBorrowedError) as e:
                print(f"Output: error message -> {e}")

      
        elif choice == "4":
            book_id = input("Input: Book ID: ")
            try:
                loan = service.return_book(book_id)
                print(f"Output: \"{loan.book.title}\" has been successfully returned.")
            except (BookNotFoundError, LoanNotFoundError) as e:
                print(f"Output: error message -> {e}")

    
        elif choice == "5":
            books = service.view_books()
            if not books:
                print("Output: \"No books found.\"")
            else:
                print("Output: \"Books:\" header")
                for book in books:
                    status = "Available" if book.available else "Borrowed"
                    print(f"Output: \"[{book.book_id}] - {book.title} by {book.author} | ({status})\"")

      
        elif choice == "6":
            members = service.view_members()
            if not members:
                print("Output: \"No members found.\"")
            else:
                print("Output: \"Members:\" header")
                for member in members:
                    print(f"Output: \"[{member.member_id}] - {member.name} ({member.email})\"")

   
        elif choice == "7":
            loans = service.view_loans()
            if not loans:
                print("Output: \"No loans found.\"")
            else:
                print("Output: \"Loans:\" header")
                for loan in loans:
                    status = "Active" if loan.is_active else "Closed"
                    print(f"Output: \"[{loan.loan_id}] - {loan.member.name} borrowed {loan.book.title} | ({status})\"")

   
        elif choice == "8":
            print("Output: \"Program closed.\"")
            print("Execute break statement")
            print("Program execution ends (returns to operating system)")
            break
            
        else:
            print("Invalid selection. Please input a number from 1 to 8.")


if __name__ == "__main__":
    main()