
# compound interest calculator

print("Welcome to the compound interest calculator")
 
principle = 0
rate = 0
time = 0
currency = input("Enter the currency symbol of your calculation: ")

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle cannot be zero.")
    else:
        break
        
while True:
    rate = float(input("Enter the Rate amount: "))
    if rate < 0:
        print("Rate cannot be zero.")
    else:
        break
        
while True:
    time = float(input("Enter the time in years: "))
    if time < 0:
        print("Time cannot be zero.")
    else:
        break
        
total = principle * pow((1 + rate / 100), time)

print(f"Balance after {time} year/s : \n{currency} {total:.2f}")
    