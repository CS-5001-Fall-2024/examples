class Item:
    """Information about a single item stored in an inventory.
    """

    def __init__(self, name, price, sku, exp_date, quantity = 0):
        """Constuctor.

        """
        self.name = name
        self.quantity = quantity
        self.price = price
        self.sku = sku
        self.exp_date = exp_date

    def update_price(self, new_price):
        self.price = new_price


    
    def update_quantity(self, amount_change, increase = False):
        # Option 1: require the caller of the method to pass in a negative  number if
        # new quantity should be less than old quantity
        # self.quantity += amount_change

        # Option 2: add an optional parameter to indicate increase/decrease
        if increase:
            self.quantity += amount_change    
        else:
            self.quantity -= amount_change

    # Option 3
    def buy_items(self, num_to_buy):
        # TODO: make sure num_to_buy is not greater than quantity
        self.quantity -= num_to_buy

    def add_new_stock(self, new_stock_quantity):
        self.quantity += new_stock_quantity


    def __str__(self):
        return f'{self.name} - quantity: {self.quantity}; price: {self.price}; sku: {self.sku}; expiration: {self.exp_date}'