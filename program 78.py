
# Probability games
import random


choice = None
print("So you cannot make a decision.")
print("Your Choices Are: \n")
print("Flipping a coin. Enter(C)\nRolling a dice Enter(D)")

def go_again():
    while True:
        go = input("Would you like to go again (Yes/No): ").lower()
        if go =="yes":
            choice_2 = input("Coin again or Die this time? (Coin/Dice): ").lower()
            if choice_2 == "coin":
                print("Okay, Coin again.")
                return coin_flip()
            elif choice_2 == "dice":
                print("Dice it is then")
                return die()
            else:
                print
        else:
            print("Thank You for playing >>>>>>>>>>>>>>>>>>>")
            break

def coin_flip():
    coin_outcomes = ['Head', 'Tail']
    rounds = int(input("How many times would you like to flip the coin?(1-10): "))
    
    if 0 < rounds <= 10:
        total_outcomes = []
        for _ in range(rounds):
            coin_flips = random.choice(coin_outcomes)
            total_outcomes.append(coin_flips)
        print("Total Outcomes:")
        for index, outcome in enumerate(total_outcomes, start=1):
            print(f"Flip {index}: {outcome}")
        go_again()
    else:
        print("The Number of times should be above 0 and or equal to 10.\n")
        return coin_flip()
    
    
def die():
    die_outcomes = [1,2,3,4,5,6]
    die_flip = random.choice(die_outcomes)
    num_of_die = input("Do you want to flip one or to dies?: ")
    
    
def game_play():
    choice = input("\nHow would you like to leave your life to chance: ").upper()
    
    while True:
        if choice == "C":
            print(f"You chose {choice} for flipping a coin.\n")
            return coin_flip()
        elif choice == "D":
            print(f"You chose {choice} for roling a dice.\n")
            return die()
        else:
            print("Invalid Entry! Try again.")
            return
            
    

if __name__ == "__main__":
    game_play()