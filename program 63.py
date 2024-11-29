
# Implementing linked list in python using object oriented programming

# Nodes 
# 1.Value -- anything strings, integers, objects
# 2.The Next node

# Creating the node class
class LinkedListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode
        
# Unconnected Node values
node1 = LinkedListNode("10")
node2 = LinkedListNode("156")
node3 = LinkedListNode("107")
node4 = LinkedListNode("167")

# Connecting them
node1.nextNode = node2 # node 1 ----> node 2
node2.nextNode = node3 # node 2 ----> node 3
node3.nextNode = node4 # node 3 ----> node 4

# Using them
currentNode = node1

while True:
    print (currentNode.value, "-->")
    if currentNode.nextNode is None:
        print ("None")
        break
    currentNode = currentNode.nextNode