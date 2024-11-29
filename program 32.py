# Simple Rock paper scissors game.

import random

while True:
    choices = ["rock", "paper", "scissors"]
    player = None
    computer = random.choice(choices)

    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()

    if player == computer:
        print("Computer: ", computer)
        print("Player: ", player)
        print("Its a tie")
    elif player == "rock":
        if computer == "paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You Lose")
        elif computer == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You Win")
    elif player == "scissors":
        if computer == "paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You Win")
        elif computer == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You Lose")
    elif player == "paper":
        if computer == "rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You Win")
        elif computer == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You Lose")
    
    play_again = input("Play Again? (yes/No): ").lower()
    
    if play_again !="yes":
        break
    
print("Thank you for playing with me")
