
# coin flip 
import random

def flip_the_coin():
    coin_sides = ["head", "tail"]
    rounds = 10
    score = 0
    
    for _ in range(rounds):
            coin_flip = random.choice(coin_sides)
            # print("You have ten rounds in total.")
            while True:
                prediction = input("Head or Tail?: ").lower()
            
                if prediction in coin_sides:
                    break
                else:
                    print("Invalid entry. \n")
                
            if prediction == coin_flip:
                print(f"Correct. You predicted {coin_flip} correctly.")
                score += 1
            else:
                print(f"Incorrect prediction. The right prediction was, {coin_flip}")
                
            rounds -= 1
            print(f"Remaining rounds: {rounds}\n")
            
    print(f"Game over. Your score is {score}")
    
    
while True:
    flip_the_coin()
    play_again = input("Do you want to play again? (Yes/No): ").lower()
    if play_again != "yes":
        print("Thank you for playing.")
        break
    