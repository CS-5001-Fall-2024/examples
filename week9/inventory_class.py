from inventory_item import Item

class Inventory:
    """Maintains an inventory of items.

    Attributes:
      items: a dictionary of items	
          - key will be the sku (int)
          - value will be 
    """
    
    def __init__(self):
        """Constructor.
        """
        self.inventory = {}

    # Option 1
    def add_item_opt_1(self, item):
        self.inventory[item.sku] = item

    # Option 2
    def add_item_opt_2(self, name, price, sku, exp_date, quantity = 0):
        item = Item(name, price, sku, exp_date, quantity)
        self.inventory[item.sku] = item

    def purchase_item(self, sku, quantity):
        item = self.inventory[sku]
        item.buy_items(quantity)

        # self.inventory[sku].buy_items(quantity)

    def __str__(self):
        result = ''
        for item in self.inventory.values():
            result += str(item) + '\n'
        return result

    # methods to add a new item, purchase an item, and return a string
    # representation of this inventory
