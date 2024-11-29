
#logical operators
#evaluate multiple conditions (or, and, not)
#or = atleast one condition must be true
#and = both conditions must be true
# not = inverts the condition (not false, not True)

temp = int(input("Enter The Current Temperature: "))
is_Sunny = True

if temp >= 28 and is_Sunny:
    print("It is Hot Outside")
    print("It is Sunny")
elif temp <= 0 and is_Sunny:
    print("It is Cold Outside")
    print("It is Sunny")
elif temp < 28 and temp > 0 and is_Sunny:
    print("It is Hot Outside")
    print("It is Sunny")