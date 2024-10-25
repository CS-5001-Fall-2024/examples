inventory = {}

def add_new_item(new_item, number_available: int):
    """
    Add a new item to the inventory with quantity number_available.
    Raises an exception if the item is already in the 
    inventory.
    """
    if new_item in inventory:
        raise Exception(f'Item {new_item} already in inventory.')
    inventory[new_item] = number_available

def get_number_available(item_to_find) -> int:
    """
    Return the number of the given item that are available
    in the inventory.
    Raises a KeyError if the item is not found in the inventory.
    """
    return inventory[item_to_find]

def update_number_available(item_to_find, number_purchased: int):	
    """
    Update the number of the given item that are available in 
    the inventory.
    Raises an Exception if there is not a sufficient quantity 
    of the item available. 
    """
    if item_to_find not in inventory:
        raise Exception(f'Item {item_to_find} not in inventory.')
    if inventory[item_to_find] < number_purchased:
        raise Exception(f'Insufficient quantity.')
    inventory[item_to_find] = inventory[item_to_find] - number_purchased

def show_inventory():
    """
    Display the item names and amounts for all items in the
    inventory.
    """
    print('Inventory:')
    for item, quantity in inventory.items():
        print(f'\t{item} - {quantity}')

def main():    
    add_new_item('apple', 50)
    add_new_item('kiwi', 75)
    add_new_item('orange', 20)
    # add_new_item('apple', 20)
    add_new_item('blueberry', 125)
    show_inventory()
    print(get_number_available('orange'))
    # get_number_available('papaya')
    update_number_available('blueberry', 25)
    print(inventory)


if __name__ == '__main__':
    main()