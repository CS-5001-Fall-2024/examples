from inventory_item import Item
from inventory_class import Inventory

inventory = Inventory()

item1 = Item('apples', 2.50, 12345, '11/15/2024', 50)
inventory.add_item_opt_1(item1)
print(inventory)

inventory.add_item_opt_2('bananas', .33, 98765, '11/25/2024', 20)
print(inventory)

inventory.purchase_item(12345, 10)
print(inventory)

# print(item1)

# Option 1
item1.update_quantity(20)
item1.update_quantity(-10)

# Option 2
item1.update_quantity(20) # buy 20 apples
item1.update_quantity(10, True) # add 20 apples to inventory

# Option 3
item1.add_new_stock(20) # 20 more apples in stock
item1.buy_items(10) # purchase 10 apples