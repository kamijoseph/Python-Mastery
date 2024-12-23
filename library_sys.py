
# Library management sys
print("This is The Fate's Algorithm Library")

# Book Class
class Book:
    def __init__(self, title, author, genre, isbn):
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn
        
    def __str__(self):
        return f"{self.title} by {self.author} ({self.genre}, ISBN{self.isbn})"

# Member Class   
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)
        
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            
    def __str__(self):
        borrowed = ', '.join([book.title for book in self.borrowed_books]) if self.borrowed_books else "No books borrowed"
        return f"Member: {self.name} (ID: {self.member_id}) Borrowed books: {borrowed}"
    
# Library class
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []
        
    def add_book(self, book):
        self.books.append(book)
        
    def remove_book(self, isbn):
        for book in self.books:
            if self.isbn == isbn:
                self.books.remove(book)
                return True
        return False
    
    def register_member(self, member):
        self.members.append(member)
        
    def lend_book(self, isbn, member_id):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.isbn == isbn ), None)
        
        if not member:
            print("Member Not Found")
            return
        
        if not book:
            print("Book Not Found or Unavailable")
            return
        
        member.borrow_book(book)
        self.books.remove(book)
        print(f"{book.title} has been lent to {member.name}.")
        
    def return_book(self, isbn, member_id):
        member = next((m for m in self.members if m.member_id == member_id), None)
        if not member:
            print("Member Not Found!")
            return
        
        book = next((b for b in self.books if b.isbn == isbn), None)
        if not book:
            print("Book Not Found or Unavailable!")
            return
            
        member.return_book(book)
        self.books.append(book)       
        print(f"{book.title} has been returned by {member.name}")  
        
    def display_books(self):
        if not self.books:
            print("No books Available!")
        else:
            print(f"Books Available in {self.name}: ")
            for book in self.books:
                print(book)
