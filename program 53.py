
# for loops practice

exp = [3340, 3500, 3100, 4100, 3980]
total = 0

for i in range(len(exp)):
    print("Month: ", (i+1), "Expence: ", exp[i])
    total = total + exp[i]
    
print("Total expense is: ", total)

for item in exp:
    total = total + item
print(total)

for i in range(1, 11):
    print(i*i)
    
    
key_location = "Chair"
locations = ["Garage", "Living room", "Chair", "closet"]

for i in locations:
    if i == key_location:
        print("Key is found in", i)
        break
    else:
        print ("Key is not found in", i)
        
for i in range(1, 6):
    if i%2 == 0:
        continue
    print(i*i)
    
