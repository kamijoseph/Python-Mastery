
# Python Banking Program

def show_balance(balance):
    print(f" Your Balance is ksh. {balance:.2f}")

def deposit():
    amount = float(input("Enter the amount to be deposited: "))
    
    if amount < 0:
        print("That is not a valid amount.")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter the amount to be witdrawn: ")) 
    
    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("Amount must be above 0")
        return 0
    else:
        return amount

def the_bank():
    balance = 0
    is_running = True

    while is_running:
        print("Banking Program")
        print("1.Show balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
    
        choice = input("Enter your choice (1-4): ")
    
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("That is not a valid option")
        
            
    print("Thank You For Banking With Us")

if __name__ == '__main__':
    the_bank()