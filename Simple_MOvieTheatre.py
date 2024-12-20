
# Movie Class
class Movie:
    def __init__(self, title, duration, genre):
        self.title = title
        self.duration = duration
        self.genre = genre
        
    def __str__(self):
        return f"{self.title}, ({self.genre}, {self.duration} minutes)"