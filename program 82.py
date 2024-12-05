
#Python decorators
# A function that extends the behaviour of another function without modifying the base function.
# Passes the base function as an argument to the decorator.

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("*Add your sprinkles friend.*")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("*Add your desired fudge friend*")
        func(*args, **kwargs)
    return wrapper

@add_fudge
@add_sprinkles        
def get_ice_cream(flavor):
    print(f"Here is your {flavor} Ice Cream budd")
    
get_ice_cream("Chocolate")