# Create a Restaurant class that handles all of the following dynamically
class Restaurant():
    def __init__(self, order_up = "ready", menu = "items", customer = "user_input", total_cost = 0):
        self.customer = customer
        self.menu = menu 
        self.order_up = order_up
        self.total_cost = total_cost

# consumer choice and name for order 
    def add_customer_name(self, name):
        self.customer["name"] = name 
    def add_items(self,items):
        self.items.append(items)
    def get_total_cost(self):
        index = 0
        total_cost = 1

    while index < len(self.menu):
        self.total_cost += self.items[index], ["total_cost"]
        index += 1

first_order = order_up(True)

first_order.add_consumer_name("Debbie")

# dictionary created for the items on the list
first_order.add_item({"Spinach", 10}, 
{"Avocado", 8},
{"Guava_juice, 6"}, 
{"fresh_cabbage", 12}, 
{"dressing", 2})
first_order.sort()











       



