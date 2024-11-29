
# Number guessing game

import random

print("Welcome to the number guessing game.")

name = input("What is your name?: ")

# The actual game function
def the_game():
    
    number = random.randint(1, 100)
    
    while True:
        try:
            user_guess = int(input("Enter your guess in number: "))
        except ValueError:
            print ("Please enter a vvalid number.")
            
        if user_guess < number:
            print ("Too low. Try again.")
        elif user_guess > number:
            print ("Too high. Try again.")
        elif user_guess == number:
            print (f"That is correct {name}")
            break
        
    play_again()
    
    

# Play again function
def play_again():
    
    while True:
        
        again = input(f"Would you like to play again {name}? (Yes/No): ").lower()
        
        if again == "yes":
            return the_game()
        elif again == "no":
            break
        else:
            ("Invalid Entry!")
            return play_again()
   
# The main function to call the game function.
def main():
    while True:
        print("-----------------------------------------------------------------")
        print(f"The game is simple {name}, I give you a number between 1 to 100.")
        proceed = input(f"You have to guess the correct number. Would you like proceed, {name}? (Yes/No): ").lower()
        
        if proceed == "yes":
            return the_game()
        elif proceed == "no":
            break
        else:
            print(f"Invalid entry {name}!")


main()