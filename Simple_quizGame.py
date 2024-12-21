
# Quiz Game

# new game function
def new_game():
    
    guesses = []
    correct_guesses = 0
    question_num = 1
    
    for key in questions:
        print("-----------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)
        
        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
        
    display_score(correct_guesses, guesses)

# the check answer function
def check_answer(answer, guess):
    
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0
    

# display the score function
def display_score(correct_guesses, guesses):
    print("-----------------------------")
    print("RESULTS")
    print("-----------------------------")
    
    print("Answers: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()
    
    score = int((correct_guesses/len(questions))*100)
    print(f"Your Score is {str(score)}%")


# a function for the play again prompt
def play_again():
    
    rensponse = input("Do you wamt to play again? (Yes/No) ").lower()
    
    if rensponse == "yes":
        return True
    else:
        return False

questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?: ": "C",
    "Is the Earth Round?: ": "A"
}

options = [["A. Guido Van Rossum", "B. Elon Musk", "C. Bills Gate", "D. Mark Zuckerberg"],
           ["A. 1989", "B. 1991", "C. 1974", "D. 1980"],
           ["A. Lonely Island", "B. NL", "C. Monty Pyton", "D. Mark Zuckerberg"],
           ["A. True", "B. False", "C. Debatable", "D. What is Earth"]]


new_game()

while play_again():
    new_game()
    
print("Play again soon .Good Bye")