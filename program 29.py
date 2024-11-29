
#basic file detection methods

import os

path = "c:\\Users\\OWNER\\OneDrive\\Desktop\\test.txt"

if os.path.exists(path):
    print("That location does exist")
    if os.path.isfile(path):
        print("That is a file")
else:
    print("That location doesnt exist")
