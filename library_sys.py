
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