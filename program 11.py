
# if Statements - Execute if the condition is true. For desicion making purpose.

age = int(input(" Enter Your Age: "))
has_ticket = False
price = float(10)

if has_ticket:
    print("You may Enter. You have a ticket")
else:
    print("You need to buy a ticket")

if age >= 60:
    print("You are a senior citizen")
    print(f"The ticket price for a Senior citizen is {price * 0.75}")
elif age >= 18:
    print("You are an adult")
    print(f"The ticket price for an adult is {price}")
else:
    print("You are a child")
    print(f"The ticket price for an child is {price * 0.5}")
    