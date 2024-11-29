
# lists [] = mutable, most flexible
# tuple () = immutable, faster
# set {} = mutable (add/remove), unordered

#lists
fruits = ["apple", "orange", "banana", "coconut"]

#fruits[3] = "mango"
fruits.append("mango")
fruits.remove("banana")
fruits.pop(0)
fruits.clear()

for fruit in fruits:
    print(fruit, end = ' ')
    
#tuples
fruits = ("apple", "orange", "banana", "coconut")


for fruit in fruits:
    print(fruit, end = ' ')
    
    
#set
fruits = {"apple", "orange", "banana", "coconut"}


for fruit in fruits:
    print(fruit, end = ' ')