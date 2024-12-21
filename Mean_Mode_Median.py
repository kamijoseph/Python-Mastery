#Implementing the mean, mode and median in python.

# The mean Function block
def mean(list_of_numbers):
    total = 0
    for num in list_of_numbers:
        total = total + num
    return total / len(list_of_numbers)

#The mode function block
def mode(list_of_numbers):
    max_count = (0, 0)
    for num in list_of_numbers:
        occurences = list_of_numbers.count(num)
        if occurences > max_count[0]:
            max_count = (occurences, num)
    
    return max_count[1]

#The median function block
def median(list_of_numbers):
    list_of_numbers.sort()
    N = len(list_of_numbers)
    
    #if the length N is odd
    if N % 2 == 1:
        return list_of_numbers[N // 2]
    
    #if the length N is even
    elif N % 2 == 0:
        num1 = list_of_numbers[N // 2 - 1]
        num2 = list_of_numbers[N // 2]
        
        mean = (num1 + num2) / 2
        
        return mean

numbers = [14,15,18,20,13,17,19,20]

print(mean(numbers))
print(mode(numbers))
print(median(numbers))