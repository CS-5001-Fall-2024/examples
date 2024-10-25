

def get_value(my_dictionary, key):
    """Returns the value associated with the key
    Raises:
      KeyError if key does not exist in my_dictionary
    """
    return my_dictionary[key]
    # try:
    #     value = my_dictionary[key]
    # except KeyError as ke:
    #     raise KeyError("Error")
    # return value

mapping = {'a': 1, 'b': 2}
try:
    print(get_value(mapping, 'c'))
except:
    # do something
