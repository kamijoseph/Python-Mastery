
# Multi-level ineritance. When a derived (child) class inerits another derived (child) class

class Organism:
    
    alive = True
    
class Animal(Organism):
    
    def eat(self):
        print("The animal is eating")
        
class Dog(Animal):
    
    def bark(self):
        print("This Dog is barking") 
        
dog = Dog()
print(dog.alive) 