
# object oriented programming learning

#objectives
# create a class(blueprint)
# class attributes
# create an instance
# instance attributes: defined in the __init__(self) function

#class
class SoftwareEngineer:
    
    #class attribute
    alias = "Keyboard magician"
    def __init__(self, name, age, level, salary):
        
        #instance attribute
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

#instance of the class
se1 = SoftwareEngineer('mark', 30, 'juniour', 5000)
print(se1.name)