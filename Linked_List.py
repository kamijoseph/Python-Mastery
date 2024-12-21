
# Implementing a linked list
# Check out more of Linked list on the my_dsa_notes repo

class Node:
    
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
class Linked_list:
    
    def __init__(self):
        self.head = None
        
    def insert_at_the_bginning(self, data):
        node = Node(data, self.head)
        self.head = node
        
    def insert_at_the_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_the_end(data)
        
        itr = self.head
        while itr.next:
            itr = itr.next
            
        itr.next = Node(data, None)
        
    def print(self):
        if self.head is None:
            print("Linked list is empty.")
            return
        
        itr = self.head
        llstr = ""
        
        while itr:
            llstr += str(itr.data)
            itr = itr.next
            
        print(llstr)
        
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count
            
        
if __name__ == "__main__":
    ll = Linked_list()
    ll.insert_at_the_bginning(5)
    ll.insert_at_the_bginning(89)
    ll.insert_at_the_end(400)
    ll.print()
    
    print("The length: ", ll.get_length())