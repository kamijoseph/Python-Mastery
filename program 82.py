
#Python decorators
# A function that extends the behaviour of another function without modifying the base function.
# Passes the base function as an argument to the decorator.

def add_sprinkles(func):
    def wrapper():
        print("*Add your sprinkles friend.*")
        func()
    return wrapper

@add_sprinkles        
def get_ice_cream():
    print("Here is your Ice Cream budd")
    
get_ice_cream()