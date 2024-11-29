
# Generating a fibonacci sequence

def fibonacci(n):
    sequence = []
    a, b = 0, 1
    
    for _ in range(n):
        sequence.append(a)
        a, b = b, a+b
    return sequence

while True:
    n = input("Enter the amount of fib numbers you want to generate: ")
    
    if n.isdigit() and int(n) > 0:
        n = int(n)
        break
    print("Invalid ! Input only takes integers above 0.")

result = fibonacci(n)
print(result)