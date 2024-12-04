
# Understanding for loops in python.

# 1
def one():
    
    word = "Python"
    for letter in word:
        print(letter)
    
# 2
def two():
    numbers = [1,2,3,4,5,6,7,8,9,10]

    for num in numbers:
        if num % 2 == 0:
            print(f"Number {num} is even.")
        else:
            print(f"Number {num} is odd.")

# 3 
def three():
    names =["Beverly", "Precious", "Wangari" "Josphat", "Njogu", "Kiarie"]

    for index, name in enumerate (names):
        print(f"{index}: {name}")
        
# 4
def four():
    sum = 0
    for i in range(1, 11):
        sum += i
    print(sum)
    
# 5
def five():
    for i in range(1, 4):
        for j in range (1, 4):
            print(f"{i} * {j} = {i*j}")

# 6
def six():
    for i in range(1, 5):
        for j in range(i):
            print("*", end=" ")
        print()

# 7
def seven():
    for i in range(1, 5):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
        
