
# Library management sys
print("This is The Fate's Algorithm Library")

class Book:
    def __init__(self, title, author, genre, isbn):
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn
        
    def __str__(self):
        return f"{self.title} by {self.author} ({self.genre}, ISBN{self.isbn})"