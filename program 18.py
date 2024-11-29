
#" dictionary
# its a changeable, unordered collection of unique key: 
# value pairs fast because they use hashing, allow us to access a value quickly"

capitals = {'USA':'washington DC',
            'India':'New delhi',
            'China':'Beijing',
            'Russia':'Moscow'}

#print(capitals['Russia'])

print(capitals.get('Germany'))

for key,value in capitals.items():
    print(key, value)