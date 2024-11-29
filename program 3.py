
import csv

class Item:
    pay_rate = 0 #The pay rate after discount
    all = []
    def __init__(self, name: str, price: float, quantity: int):
        
        #Run validations to the received arguments
        assert price > 0, f"Price {price} is not greater than zero"
        assert quantity > 0, f"Quantity {quantity} is not greater than zero"
        
        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        #Action to execute
        Item.all.append(self)
        
    def calculate_total_price (self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instatiate_from_csv(cls):
        with open('item.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            print(item)
    
    def __repr__(self):
        return f"Item('{self.name}', '{self.price}', '{self.quantity}')"
        


Item.instatiate_from_csv()