
# Binomial distribution calculator.
from math import comb

#binomial distribution function.

def binomial_distribution():
    print ("=== Binomial Distribution Calculator === \n")
    print ("=== Solution must have a binary outcome ===")
    print ("=== Trials should be indipendent ===")
    print ("=== Number of trials should be included ===")
    print ("=== The probability of each trial should be equal ===")
    print ("=== The probability should be between 0 and 1 ===\n")
    
    #Checking for invalid numerical value
    
    while True:
        try:
            #Ask for user inputs
            n = int(input("Enter the number of trials (n): "))
            k = int(input("Enter the number of success (K): "))
            p = float(input("Enter the probability of success in a single try (p): "))
            
            #Validating if the probability is between 0 and 1
            if not (0 <= p <= 1):
                print("Error: Probability must be between 0 and 1")
                return
            
            #Checking if the number of successe is <= number of trials and >= 0
            if not (0 <= k <= n):
                print("Number of successes cannot be above number of trials and below 0")
                return
            
            # Computing the binomial distribution
            probability = comb(n, k) * (p**k) * ((1-p)**(n-k))
            
            #Display the results
            print(f"\nThe probability of getting exactly {k} number of successes in {n} number of trials is {probability: .6f}")
            
            #Returning the try except ValueError
        except ValueError:
            print("Please enter valid numerical numbers!")
        
        #Ask if user want to play to calculate again.
        choice = input("\nWould you like to perform more calculations (Yes/No): ").strip().lower()
        
        if choice != "yes":
            print("\nExiting the Binomial distribution Calculator. Goodbye!")
            break

if __name__ == "__main__":
    binomial_distribution()