
# Iterators
# iterating through and through. i have no idea what that even means

nums = [1, 2, 3, 4, 5]
it = iter(nums)

print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())

# With Objects
class TopTen:
    def __init__(self):
        self.num = 1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration
    
values = TopTen()
for i in values:
    print(i)