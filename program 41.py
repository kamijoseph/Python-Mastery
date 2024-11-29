 # python weight converter

def main():
     
    def main_for_weight():
        
        run_again
        weight = float(input("Enter your weight: "))
        unit= input("Kilograms or Pound (K or L): ").upper()

        if unit == "K":
            weight = weight * 2.205
            unit = "Lbs"
        elif unit == "L":
            weight = weight / 2.205
            unit = "Kgs"
        else:
            print(f"{unit} was not valid")
            
        print(f"Your weight is: {weight} {unit} ")
        
        

    # def run_again():
        
    #     weight_run_again = input("Would you like to convert more weight? (Y/N): ").upper()
    #     if weight_run_again == "Y":
    #         return main_for_weight()
    #     elif weight_run_again == "N":
    #         return False
    #     else:
    #         print("Invalid entry! Try again.")
            
if __name__ == "__main__":
     main()