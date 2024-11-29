
# Dice Rolling Game
# My way

import random

print("Welcome to the dice rolling game")
print("---------------------------------\n")
def dice_roll():
    
    rolls = [1, 2, 3, 4, 5, 6]
    dice_1 = None
    dice_2 = None
    is_running = True
    
    while is_running:
        print("----------------------------------")
        roll_choice = input("Roll with R, Stop with S: ").upper()
        
        if roll_choice == "R":
            dice_1 = random.choice(rolls)
            dice_2 = random.choice(rolls)
            print (f"Your Roll result is: [{dice_1}, {dice_2}]")
            print ("-----------------------------------")
        elif roll_choice == "S":
            is_running = False
        else:
            print("Invalid entry!!")    
            return dice_roll()
        
def main():
    while True:
        
        play = input("To play press P to exit press E: ").upper()
        
        if play == "P":
            return dice_roll()
        else:
            print("-----------------------------------------\n")
            print("Thank you for playing. Welcome back later" )
            break
        
if __name__ == "__main__":
    main()