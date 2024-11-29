
#"Keyword arguments = arguments preceeded by an identifier when we pass them to a function
# The order of the arguments doesnt matter, unlike positional arguments.
# Python knows the names of the argument that 0ur function receives"

def hello (first,middle,last):
    print(f"Hello {first} {middle} {last}")
    
    
hello(middle="Kami", first="Leonardo",last="Joseph")