
# GeneratorS

def topten():
    n = 1
    
    while n <= 10:
        sq = n*n
        yield sq
        n += 1

values = topten()
print(values.__next__())

for j in values:
    print(j)