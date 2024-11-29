
#variable scopes
# the region that a variable is recognized
# a variable is only available from inside te region it is created
# a global and locally available scopped version of a version can be created.

name = "Bro" #a global scope (Available inside and outside a variable)
def display_name():
    name = 'code' #local scope(Available only inside this function)
    print(name)
    
print(name)
display_name()
