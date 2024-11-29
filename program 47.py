
# Shopping cart program

foods = []
prices = []
total = 0.0

while True:
    food = input("Enter a food to buy or q to exit: ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)
        
print("---------- YOUR CART ----------")

for food in foods:
    print(food)
for price in prices:
    total= float(total) + price
    
print("\n")
print(f"Your total is: ${total}")