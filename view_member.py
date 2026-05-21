class Member:
    def __init__(self, member_id: str, name: str, email: str):
        self.member_id = member_id
        self.name = name
        self.email = email

class LibraryService:
    def __init__(self):
        self._members = {}

    def view_members(self):
        return list(self._members.values())


service = LibraryService()
choice = "6"

if choice == "6":
    members = service.view_members()
    if not members:
        print("Output: \"No members found.\"")
    else:
        print("Output: \"Members:\" header")
        for member in members:
            print(f"Output: \"[{member.member_id}] - {member.name} ({member.email})\"")