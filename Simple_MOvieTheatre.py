
# A Simple Movie Theatre Management System

# Movie Class
class Movie:
    def __init__(self, title, duration, genre):
        self.title = title
        self.duration = duration
        self.genre = genre
        
    def __str__(self):
        return f"{self.title}, ({self.genre}, {self.duration} minutes)"
    
# Ticket Class
class Ticket:
    def __init__(self, movie_title, screen_number, seat_number):
        self.movie_title = movie_title
        self.screen_number = screen_number
        self.seat_number = seat_number
        
    def __str__(self):
        return f"Movie: {self.movie_title}, Screen: {self.screen_number}, seat: {self.seat_number}"
    
# Screens Class
class Screen:
    def __init__(self, screen_number, capacity):
        self.screen_number = screen_number
        self.capacity = capacity
        self.booked_seats = 0
        self.movie = None
        self.tickets = []
        
    def assign_movie(self, movie):
        self.movie = movie
        
    def book_ticket(self, num_tickets):
        if self.booked_seats + num_tickets <= self.capacity:
            for i in range(1, num_tickets + 1):
                seat_number = self.booked_seats + i
                ticket = Ticket(self.movie.title, self.screen_number, seat_number)
                self.tickets.append(ticket)
            self.booked_seats += num_tickets
            print(f"{num_tickets} tickets booked successfully for {self.movie.title} on Screen {self.screen_number}.")
        else:
            print("Not enough seats available.")
            
    def display_tickets(self):
        print(f"Tickets for screen {self.screen_number}: ")
        for ticket in self.tickets:
            print(ticket)
            
    def __str__(self):
        movie_info = self.movie if self.movie else "No Movie Assigned"
        return f"Screen {self.screen_number}: {movie_info}, Seats booked: {self.booked_seats}/{self.capacity}"
    
# Movie Theatre Class
class MovieTheatre:
    def __init__(self, name):
        self.name = name
        self.screens = []
        
    def add_screen(self, screen):
        self.screens.append(screen)
        
    def show_movies(self):
        print(f"Movies currently playing at {self.name}: ")
        for screen in self.screens:
            print(screen)
            
    def find_screen(self, screen_number):
        for screen in self.screen:
            if screen == self.screen_number:
                return screen
        print("Screen Not Found!")
        return None
    
# Application Usage
if __name__ == "__main__":
    
    #Create Theatre
    theatre = MovieTheatre("IMAX Studios")
    
    #Create Some Movies
    movie1 = Movie("The Boys", 136, "Fantasy fiction")
    movie2 = Movie("Home Alone", 145, "Drama")
    movie3 = Movie("Shadow Hunters", 300, "Fantasy fiction")
    movie4 = Movie("50 Shades Black", 203, "Sex Romance")
    movie5 = Movie("Rick And Morty", 480, "Sci-Fi Adventure")
    
    #Create Some Screen and Assign Movies
    screen1 = Screen(1, 100)
    screen1.assign_movie(movie1)
    screen2 = Screen(2, 100)
    screen2.assign_movie(movie2)
    screen3 = Screen(3, 100)
    screen3.assign_movie(movie3)
    screen4 = Screen(4, 100)
    screen4.assign_movie(movie4)
    screen5 = Screen(5, 100)
    screen5.assign_movie(movie5)

    #Add screen to the theatre
    theatre.add_screen(screen1)
    theatre.add_screen(screen2)
    theatre.add_screen(screen3)
    theatre.add_screen(screen4)
    theatre.add_screen(screen5)
    
    #Display all movies
    theatre.show_movies()
    
    #Book Tickets
    screen1.book_ticket(5)
    screen2.book_ticket(34)
    screen3.book_ticket(40)
    screen4.book_ticket(11)
    screen5.book_ticket(8)
    
    #Show Tickets
    screen1.display_tickets()
    screen2.display_tickets()
    screen3.display_tickets()
    screen4.display_tickets()
    screen5.display_tickets()
    
    #Show Updated Movies
    theatre.show_movies()