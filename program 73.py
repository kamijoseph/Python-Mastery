
# Rolling a dice to simulate discrete probability mass function random variables.
import random

def roll_dice():
    return random.randint(1, 6)

rolls = [roll_dice() for _ in range(10)]

print("Rolls:", rolls)

#Exercise 
# Modify the code above to ask for user input to roll two dies ten times
# Return a list of the rolled die outcome