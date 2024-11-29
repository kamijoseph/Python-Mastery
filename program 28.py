
# exception = events detected during execution that interrupt the flow o a program.

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator/denominator
except(ZeroDivisionError) as e:
    print(e)
    print("You cannot divide by zero dumbass!")
except ValueError as e:
    print(e)
    print("Enter only a number please")
except Exception as e:
    print(e)
    print("Something went wrong!")
else:
    print(result)
finally:
    print("This will always execute")