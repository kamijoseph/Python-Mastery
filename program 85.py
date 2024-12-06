
# Multithreding with python
# Used to perfom multiple tasks concurrently(Multi-tasking)
# Good for I/O tasks like reading files or fetching data from API's
# Thread(target=my_function)

import threading
import time

def walk_the_dog(first, last):
    time.sleep(9)
    print(f"You finish walking {first} {last}.")

def take_out_trash():
    time.sleep(3)
    print("\nYou take out the trassh.")
    
def get_mail():
    time.sleep(5)
    print('Get the mail.')
    
chore1 = threading.Thread(target=walk_the_dog, args=("Scooby", "Doo"))
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("\nAll tasks complete.\n")