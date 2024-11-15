"""
A class that implements the Stack data structure.
"""
class Stack:

    def __init__(self, max_size):
        """Constructor
        
        Parameters:
        max_size -- max number of items in the stack
        """
        self.items = []
        self.max_size = max_size

    def push(self, item):
        """ Adds a new item to the top of the stack

        Parameters:
        item -- the item to add

        Raises:
        Exception -- if the stack is full

        """
        if len(self.items) == self.max_size:
            raise Exception('Stack full!')
        self.items.append(item)


    def pop(self):
        """ Retrieves and returns the top item.

        Returns:
        item -- top item in the stack

        Raises:
        Exception -- if the stack is empty
        """
        if len(self.items) == 0:
            raise Exception('Stack is empty!')
        item = self.items.pop()
        return item

    def size(self):
        """ Returns the number of items in the stack.
        """
        return len(self.items)
    

    def debug(self):
        """ Debug method to print all items in the stack.
        """
        print(self.items)