
try:
    with open("c:\\Users\\OWNER\\OneDrive\\Desktop\\test.txt")as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found")
    
