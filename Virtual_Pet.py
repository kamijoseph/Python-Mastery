
#----------Virtual Pet Game----------
import time

# VirtualPetClass
class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50
        self.energy = 50
        
    def feed(self):
        if self.hunger > 0:
            self.hunger -= 10
            self.happiness += 5
            print(f"You fed {self.name}. Hunger decreased, happiness increased")
        else:
            print(f"self.name is already full.")
    
    def play(self):
        if self.energy >= 10:
            self.happiness += 10
            self.energy -= 10
            self.hunger += 5
            print(f"You played with {self.name}. Happiness increased. Energy and Hunger Levels adjusted.")
        else:
            print(f"{self.name} too tired to play. Let them rest.")
            
    def rest(self):
        if self.energy < 100:
            self.energy += 20
            self.hunger += 5
            print(f"{self.name} is resting. Energy Increased.")
        else:
            print(f"{self.name} is already full of energy.")
            
    def status(self):
        print(f"\n------------{self.name}'s Status------------")
        print(f"Hunger: {self.hunger}/100")
        print(f"Energy: {self.energy}/100")
        print(f"Happiness: {self.happiness}/100")
        print("------------------------------------------------\n")
        
    def is_alive(self):
        if self.hunger >= 100:
            print(f"{self.name} has starved to death. Game Over!")
            return False
        if self.happiness >= 100:
            print(f"{self.name} is too unhappy. {self.name} has run over. Game Over")
            return False
        return True

def main():
    print("Welcome to the Virtual Pet Game.")
    pet_name = input("Enter the name of your Pet: ")
    pet = VirtualPet(pet_name)
    
    while pet.is_alive():
        pet.status
        print("What would you like to do?")
        print("1. Feed")
        print("2. Play")
        print("3. Rest")
        print("4. Do nothing")
        
        choice = input("Enter Your choice (1-4): ")
        if choice == "1":
            pet.feed()
        elif choice == "2":
            pet.play()
        elif choice == "3":
            pet.rest()
        elif choice == "4":
            print(f"{pet.name} waits patiently........")
            pet.hunger += 5
            pet.happiness -= 5
        else:
            print("Invalid choice. Please try again.")
        time.sleep(2)
    print("Thank You for playing.")

if __name__ == "__main__":
    main()