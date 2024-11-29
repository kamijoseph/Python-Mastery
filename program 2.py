
class Item:
    pay_rate = 0 #The pay rate after discount
    def __init__(self, name: str, price: float, quantity: int):
        
        #Run validations to the received arguments
        assert price > 0, f"Price {price} is not greater than zero"
        assert quantity > 0, f"Quantity {quantity} is not greater than zero"
        
        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def calculate_total_price (self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
        

item1 = Item("phone", 100, 5)
item2 = Item("laptop", 1000, 3)

item1.pay_rate = 0.8
item1.apply_discount()
item2.pay_rate = 0.7
item2.apply_discount()

print(item1.price)
print(item2.price)


