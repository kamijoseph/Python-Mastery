
# Class Variable

class Car:
    
    #class variable
    wheels = 4
    
    #init method
    def __init__(self,make,model,year,color):
        
        #instance variables
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        
car_1 = Car("Chevy","Corvette",2021,"blue")
car_2 = Car("Ford","Mustang",2022,"red")

car_1.wheels = 2

print(car_1.wheels)