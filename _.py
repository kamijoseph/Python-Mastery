import random

def go_again():
    while True:
        go = input("\nWould you like to go again (Yes/No): ").lower()
        if go == "yes":
            choice_2 = input("Coin again or Dice this time? (Coin/Dice): ").lower()
            if choice_2 == "coin":
                print("Okay, flipping the coin again!")
                return coin_flip()
            elif choice_2 == "dice":
                print("Rolling the dice this time!")
                return die()
            else:
                print("Invalid choice. Please choose 'Coin' or 'Dice'.")
        elif go == "no":
            print("\nThank you for playing! >>>>>>>>>>>>>>>>>>>")
            break
        else:
            print("Invalid entry! Please type 'Yes' or 'No'.")

def coin_flip():
    coin_outcomes = ['Head', 'Tail']
    rounds = int(input("\nHow many times would you like to flip the coin? (1-10): "))
    
    if 0 < rounds <= 10:
        total_outcomes = []
        for _ in range(rounds):
            coin_flips = random.choice(coin_outcomes)
            total_outcomes.append(coin_flips)
        print("\nTotal Outcomes:")
        for index, outcome in enumerate(total_outcomes, start=1):
            print(f"Flip {index}: {outcome}")
        go_again()
    else:
        print("The number of flips must be between 1 and 10.\n")
        return coin_flip()

def die():
    die_outcomes = [1, 2, 3, 4, 5, 6]
    num_of_dice = input("\nDo you want to roll one or two dice? (1/2): ")
    
    if num_of_dice == "1":
        result = random.choice(die_outcomes)
        print(f"\nYou rolled a single die: {result}")
    elif num_of_dice == "2":
        result = [random.choice(die_outcomes), random.choice(die_outcomes)]
        print(f"\nYou rolled two dice: {result[0]} and {result[1]} (Total: {sum(result)})")
    else:
        print("Invalid input! Please enter 1 or 2.")
        return die()
    go_again()

def game_play():
    print("Welcome to the Probability Games!")
    print("Your Choices Are:")
    print("Flipping a Coin: Enter 'C'")
    print("Rolling a Dice: Enter 'D'")

    while True:
        choice = input("\nHow would you like to leave your fate to chance? (C/D): ").upper()
        if choice == "C":
            print("\nYou chose to flip a coin!")
            return coin_flip()
        elif choice == "D":
            print("\nYou chose to roll a dice!")
            return die()
        else:
            print("Invalid entry! Please choose 'C' or 'D'.")

if __name__ == "__main__":
    game_play()
