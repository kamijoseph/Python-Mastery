
#while loops
#used to repeat a block of code as long as a condition remains true

name = input("Enter Your Name: ")

while name == "":
    name = input("Enter Your Name: ")
    
age = int(input("Enter Your Age: "))

while age < 0:
    print("Age cannot be zero.")
    age = input("Enter Your Age: ")
    
print(f"Hello {name}! You are {age} years old")
