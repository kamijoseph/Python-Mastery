
#"loop control statements = change a loops from its normal sequence

#break = used  to terminate the loop entirely
# continue = Skips to the next itertion of the loop
# pass = does nothing, acts as a placeholder"

while True:
    name = input("Enter Your Name: ")
    if name != "":
        break 
    
for i in range (1,21):
    
    if i == 13:
        pass
    else:
        print(i) 