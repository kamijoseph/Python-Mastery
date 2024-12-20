#python project

name = input("What is your name: ")
print(f"Welcome to the program{name}. Your task is to guess the hidden name.")
print("I will give you three hints and you have three tries")

hidden_name = "rick"
num_of_tries = 3

print("Hint One: A drunkard cartoon character in a sci-fi themed cartton show")
print("Hint two: Has a naive sideKick sort of character who happens to be their relative")
print("Hint three: Second name begins with 'S' \n")



while num_of_tries > 0:
    guess = input("What is the character's first name: ").lower()
    if guess != "rick":
        num_of_tries -= 1
        if num_of_tries > 0:
            print(f"Incorret.{num_of_tries} tries remaining. Try again.")
        else:
            print("Incorrect, Out of tries budd. The character was Rick Sanchez from the show Rick and Morty.")
    else:
        print(f"Correct! The character was {guess} sanchez, from the show Rick & Morty.")
        break