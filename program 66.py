
# Pig
import random

def the_roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    
    return roll

while True:
    players = input("Enter the number of players.(2-4): ")
    if players.isdigit():
        players = int(players)
        
        if 2 <= players <= 4:
            break
        else:
            print("Players must be between 2 and 4")
    else:
         print("Invalid! Try again.")       
         
max_score =50
players_score = [0 for _ in range(len(players))]

while max(players) < max_score:
    for player_idx in range(players):
        print("Player", player_idx + 1, "turn have just started.")
        current_score = 0
        
        while True:
            should_roll = input("Would you like to roll (y)")
            
            if should_roll.lower() == "y":
                value = the_roll()
            else:
                break
            
            if value == 1:
                print("You rolled a one. Turn done.")
                break
            else:
                current_score += value
                print("You rolled a:", value)
                
            print("Your score is: ", current_score)
            
        players_score[player_idx] += current_score