class Item:
    """Information about a single item stored in an inventory.
    """


    def __init__(self, name, quantity, price, sku, exp_date):
        """Constuctor.

        """
        self.name = name
        self.quantity = quantity
        self.price = price
        self.sku = sku
        self.exp_date = exp_date