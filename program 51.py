
# Inheritance

#Inheritance is literally classes ineriting attributes from another class

# Code

class Vehicle:
    def general_usage(self):
        print("General use: transportation")
        
class Car(Vehicle):
    def __init__(self):
        print ("I am a car")
        self.wheels = 4
        self.has_roof = True
        
    def specific_usage(self):
        print("Specific use: Commute to work, vacation with family")
        
class Motorcycle(Vehicle):
    def __init__(self):
        print ("I am a motorcycle")
        self.wheels = 2
        self.has_roof = False
        
    def specific_usage(self):
        print("Specific use: Weekends fun and Roadtrip.")
        
small_car = Car()
small_car.general_usage()
small_car.specific_usage()

print("_____________________________")

bike = Motorcycle()
bike.general_usage()
bike.specific_usage()