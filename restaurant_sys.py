
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
        self.is_reserved = False
    
    def add_order(self, item):
        self.orders.append(item)
        
    def calculate_total(self):
        return sum(item.price for item in self.orders)
    
    def clear_table(self):
        self.orders = []
        self.is_reserved = False
        
    def reserve_table(self):
        self.is_reserved = True
        
    def __str__(self):
        if not self.orders:
            return f"Table {self.table_number} has no orders. Reserved: {self.is_reserved}"
        orders_summary = ', '.join(item.name for item in self.orders)
        total = self.calculate_total()
        return f"Table {self.table_number}: Orders: {orders_summary} | Total: ${total:.2f} | Reserved: {self.is_reserved}"
    
class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = []
        self.tables = []
        
    def add_menu_item(self, item):
        self.menu.append(item)
        
    def add_table(self, table):
        self.tables.append(table)
        
    def show_menu(self):
        print(f"\n--- {self.name} Menu ---")
        for item in self.menu:
            print(item)
        print("----------------------\n")
        
    def show_tables(self):
        print(f"\n--- {self.name} Tables ---")
        for table in self.tables:
            print(table)
        print("----------------------\n")
    
    def take_order(self, table_number, item_name):
        table = next((t for t in self.tables if t.table_number == table_number), None)
        if not table:
            print(f"Table {table_number} not found.")
            return
        
        item = next((i for i in self.menu if i.name == item_name), None)
        if not item:
            print(f"Menu {item_name} not found.")
            return
        
        table.add_order(item)
        print(f"Added {item_name} to Table {table_number}")
        
# Application Example
if __name__ == "__main__":
    # Create a restaurant
    restaurant = Restaurant("Fate's Algorithm Restaurant")

    # Add menu items
    restaurant.add_menu_item(MenuItem("Burger", 8.99))
    restaurant.add_menu_item(MenuItem("Pasta", 12.99))
    restaurant.add_menu_item(MenuItem("Salad", 6.99))
    restaurant.add_menu_item(MenuItem("Soda", 1.99))

    # Add tables
    restaurant.add_table(Table(1))
    restaurant.add_table(Table(2))

    # Display menu and tables
    restaurant.show_menu()
    restaurant.show_tables()

    # Take orders
    restaurant.take_order(1, "Burger")
    restaurant.take_order(1, "Soda")
    restaurant.take_order(2, "Pasta")

    # Show tables after orders
    restaurant.show_tables()

    # Clear table
    restaurant.tables[0].clear_table()
    print("\nAfter clearing Table 1:")
    restaurant.show_tables()