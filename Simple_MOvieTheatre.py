
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