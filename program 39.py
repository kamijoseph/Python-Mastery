 # choice Barista
 
print("Welcome to our fine establishment")
customer = input("What is your name: ").lower()
menu = "espresso, capuccino, black choice, latte, white choice, frapuccino."

print(f"Menu = {menu}")

def order():
    choice = input(f"What would you like to order today, {customer}: ")
    if choice == "espresso":
        print("The price is $10 2f")
    elif choice == "capuccino":
        print("The price is $8 2f")
    elif choice == "black choice":
        print("The price is $5 2f") 
    elif choice == "latte":
        print("The price is $9 2f")
    elif choice == "white choice":
        print("The price is $8 2f")
    elif choice == "frapuccino":
        print("The price is $11 2f")
    else:
        print("Sorry! That is not on the menu. Check spelling")
    


is_running = True
while is_running:
    
    want = input(f"Would you like to order? {customer} (yes/no): ").lower()
    
    if want == "yes":
        order()
    else:
        is_running = False
    
    
    