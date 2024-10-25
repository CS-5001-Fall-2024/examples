inventory_item = []
inventory_quantity = []

def add_new_item(new_item, number_available: int):
    """
    Add a new item to the inventory with quantity number_available.
    Raises an exception if the item is already in the 
    inventory.
    """
    # if new_item not in inventory_item:
    #     inventory_item.append(new_item)
    #     inventory_quantity.append(number_available)
    # else:
    #     raise Exception('Item already in inventory.')

    if new_item in inventory_item:
        raise Exception(f'Item {new_item} already in inventory.')
    inventory_item.append(new_item)
    inventory_quantity.append(number_available)
    

def get_number_available(item_to_find) -> int:
    """
    Return the number of the given item that are available
    in the inventory.
    Raises a KeyError if the item is not found in the inventory.
    """

    # Oops! I used find, but I should have used index.
    # All of the same comments about running time apply.
    location = inventory_item.index(item_to_find)
    if location == -1:
        raise KeyError(f'Item {item_to_find} not found.')
    return inventory_quantity[location]

    # for i in range(len(inventory_item)):
    #     if inventory_item[i] == item_to_find:
    #         return inventory_quantity[i]
    # raise KeyError(f'Item {item_to_find} not found.')

def update_number_available(item_to_find, number_purchased: int):	
    """
    Update the number of the given item that are available in 
    the inventory.
    Raises an Exception if there is not a sufficient quantity 
    of the item available. 
    """
    found = False
    for i in range(len(inventory_item)):
        if inventory_item[i] == item_to_find:
            found = True
            if number_purchased > inventory_quantity[i]:
                raise Exception(f'Insufficient quantity.')
            inventory_quantity[i] = inventory_quantity[i] - number_purchased
            break
    if not found:
        raise Exception(f'Item {item_to_find} not in inventory.')
            

def show_inventory():
    """
    Display the item names and amounts for all items in the
    inventory.
    """
    print('Inventory:')
    for item, quantity in zip(inventory_item, inventory_quantity):
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
    show_inventory()




if __name__ == '__main__':
    main()