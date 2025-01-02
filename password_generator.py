
# Simple password generator with random and strings modules
import random
import string

def generate_password(length):
    if length < 4:
        raise ValueError("Password length must be at least 4 characters for a strong password.")
    
    #Character Sets for Password
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_char = string.punctuation
    
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_char)
    ]
    
    # Fill the rest of the password length with random choices from all sets
    all_chars = uppercase + lowercase + digits + special_char
    password += random.choices(all_chars, k=length-4)
    
    # Shuffle the password to randomize character order
    random.shuffle(password)
    return ''.join(password)

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