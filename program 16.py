
#nested loops 
# inner loop will finish all f its iteration before finishing oneiteration of the "outer loop"

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))

symbol = input("Enter a symbol to use: ")

for i in range (rows):
    for j in range (columns):
        print(symbol, end="")
    print()