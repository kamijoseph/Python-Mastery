
# A password generator
def generate_password(length):
    pass

def main():
    print("Welcome to th PassWord Generator!")
    try:
        length = int(input("Enter the desired length of the password. Above 4 characters: "))
        password = generate_password(length)
        print(f"Your generated password is \n{password}")
    except ValueError as e:
        print(f"Error {e}")
    

if __name__ == "__main__":
    main()