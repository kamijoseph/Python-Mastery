class SoftwareEngineer:
    
    #class attribute
    alias = "Keyboard magician"
    def __init__(self, name, age, level, salary):
        
        #instance attribute
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    #Instance Method
    def code(self):
        pass

#instance of the class
se1 = SoftwareEngineer('mark', 30, 'juniour', 5000)
print(se1.name)
se2 = SoftwareEngineer("Kami", 40, "Senior", 10000)
print(se2)