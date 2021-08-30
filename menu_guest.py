# Create a Restaurant class that handles all of the following dynamically
class Restaurant:
    def __init__(self, order_up = "ready", menu = "items", customer = "user_input", total_cost = 0):
        self.customer = customer
        self.menu = menu 
        self.order_up = order_up
        self.total_cost = total_cost

# consumer choice and name for order 
    def add_customer_name(self, name):
        self.customer["name"] = name 
    def add_item(self,item):
        self.items.append(item)
    def get_total_cost(self):
        index = 0
        total_cost = 0
    while index < len(self.items):
        self.total_cost += self.items[index], ["cost"]


        
       



