class Book:
    def __init__(self, title: str):
        self.title = title

class Member:
    def __init__(self, name: str):
        self.name = name

class Loan:
    def __init__(self, loan_id: str, book: Book, member: Member):
        self.loan_id = loan_id
        self.book = book
        self.member = member
        self.is_active = True

class LibraryService:
    def __init__(self):
        self._loans = []

    def view_loans(self):
        return self._loans


service = LibraryService()
choice = "7"

if choice == "7":
    loans = service.view_loans()
    if not loans:
        print("Output: \"No loans found.\"")
    else:
        print("Output: \"Loans:\" header")
        for loan in loans:
            status = "Active" if loan.is_active else "Closed"
            print(f"Output: \"[{loan.loan_id}] - {loan.member.name} borrowed {loan.book.title} | ({status})\"")