# Notes
""" Python Object oriented programming

Classes, Attributes, Instances, Arguments

"""

# Code

class Human:
    def __init__(self, name, occupation):
        self.name = name
        self.occpation = occupation
        
    def do_work(self):
        if self.occpation == "tennis player":
            print(self.name, "plays tennis")
        elif self.occpation == "actor":
            print(self.name, "is an actor")
            
    def speak(self):
        print(self.name, "asks how are you?")
        
brad = Human("Brad Pitt", "actor")
brad.do_work()
brad.speak()

maria = Human("Maria Sharapova", "tennis player")
maria.do_work()
maria.speak()