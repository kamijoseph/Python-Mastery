
# my simple arithmetic calculator

print ("Welcome to my basic arithmetic calculator \n")

running = True
def calculate():
    num1 = float(input("Enter The First Number: "))
    sign_operator = input("Enter Your Operator: ")
    num2 = float(input("Enter Your second Number: "))
    
    if sign_operator == "*":
        print (num1 * num2)
    elif sign_operator == "+":
        print (num1 + num2)
    elif sign_operator == "-":
        print (num1 - num2)
    elif sign_operator == "/":
        print (num1 / num2)
    else:
        print ("Invalid Operator!")
    
while running:
    action = float(input("For calcuations enter 1, enter 2 to exit: "))
    print(" \n")
    if action == 1:
        calculate()
    else:
        running = False
    
   