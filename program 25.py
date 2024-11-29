
# Args - parameters that will pack all arguments into a tuple (*args)
#      - Useful so that a function can accept a varying amount of arguments.

def add(*args):
    sum = 0
    for i in args:
        sum += 1
    return sum

print(add(1,3,6,7,8,9,1))
