
# Restaurant Management System
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"
    
class Table:
    def __init__(self, table_number):
        self.table_number = table_number
        self.orders = []
    
    def add_order(self, item):
        self.orders.append(item)
        
    def calculate_total(self):
        return sum(item.price for item in self.orders)
    
    def clear_table(self):
        self.orders = []
        
    def __str__(self):
        if not self.orders:
            return f"{self.table_number} has no orders."
        orders_summary = ', '.join(item.name for item in self.orders)
        total = self.calculate_total()
        return f"Table {self.table_number}: Orders: {orders_summary} | Total: ${total:.2f}"