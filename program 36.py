
# Inheritance

class Animal():
    
    alive = True
    
    def eat(self):
        print("This animal is eating")
        
    def sleep(self):
        print("This animal is sleeping")
        
class Rabbit(Animal):
    
    def run(self):
        print("This rabbit is running")
        
class Fish(Animal):
    def swim(self):
        print("The fish is swimming")
        
class Hawk(Animal):
    def fly(self):
        print("The hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.sleep()