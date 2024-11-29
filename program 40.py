
#temperature converter

unit = input("Is this temperature in celcius or fahrenheit (C/F): ").upper()
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp} degrees")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in celsius is: {temp} degrees")
else:
    print(f"{unit} is an invalid unit of measurement")
    