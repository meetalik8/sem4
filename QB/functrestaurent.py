class Restaurant:
def __init__(self):
self.menu_items = {}
self.book_table = []
self.customer_orders = []
def add_item_to_menu(self, item, price):
self.menu_items[item] = price
def book_tables(self, table_number):
self.book_table.append(table_number)
def customer_order(self, table_number, order):
order_details = {'table_number': table_number, 'order': order}
self.customer_orders.append(order_details)
def print_menu_items(self):
for item, price in self.menu_items.items():
print("{}: {}".format(item, price))
def print_table_reservations(self):
for table in self.book_table:
print("Table {}".format(table))
def print_customer_orders(self):
for order in self.customer_orders:
print("Table {}: {}".format(order['table_number'], order['order']))
restaurant = Restaurant()
