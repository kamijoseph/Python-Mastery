
# an email slicer program

email = input("Enter Your email: ")


index = email.index("@")

username = email[:index]
domain = email[index:]

print(f"Your Username is {username} and domain i {domain}")