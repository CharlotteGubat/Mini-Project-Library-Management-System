class Member:
    def __init__(self, member_id: str, name: str, email: str):
        self.member_id = member_id
        self.name = name
        self.email = email

class LibraryService:
    def __init__(self):
        self._members = {}

    def register_member(self, member_id: str, name: str, email: str):
        new_member = Member(member_id, name, email)
        self._members[member_id] = new_member
        return new_member


service = LibraryService()
choice = "2"

if choice == "2":
    member_id = input("Input: Member ID: ")
    name = input("Input: Member Name: ")
    email = input("Input: Member Email: ")
    
    member = service.register_member(member_id, name, email)
    print(f"Output: \"Member registered: {member.name}\"")