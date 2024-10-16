# See: https://docs.python.org/3/library/exceptions.html
# https://docs.python.org/3/library/os.html
import os

def convert(value, target_type):
    """
    Write a function to convert value into the target type. 
    Valid type for target_type is int or float.
    If the value is already the target_type
        return the value without conversion
    If the target_type is not int or float
        generate a TypeError
    If the value cannot be converted
        generate a ValueError
    """
    # '5'
    # int
    if isinstance(value, target_type):
        return value
    
    if target_type != int and target_type != float:
        raise TypeError('You gave me an invalid type!')
    
    if target_type == int:
        new_value = int(value)
    elif target_type == float:
        new_value = float(value)
    return new_value

    
def read_file(filename: str):
    """
    Write a function to display the contents of a file.
    The function will throw an exception if the file is
    not found.
    """
    with open(filename, 'r') as input_file:
        for line in input_file:
            print(line)

def search_replace(search:str, 
    replace:str, 
    infilename:str, 
    outfilename:str):
    """
    Write a function that will replace all instances of a search
    term in a given file with a replace term. The result will be 
    saved to a new file.
    
    Parameters:
    search : str
        the string to replace
    replace : str
        the replacement string
    infilename : str
        the name of the original file
    outfilename : str
        the name of the file where the result will be saved
    """
    pass


def find_py_files(root: str):
    # /Users/srollins/teaching/cs5001-f23 
    '''
    Write a recursive function to list all files in any
    descendant directory of a given root.
    '''
    pass


def pass_by_reference(local_list: list[str]):
    local_list.append('XXX')


def main():

    read_file('error_handling.py')

    # to_convert = 4
    # print(f'Type of to_convert = {type(to_convert)}')
    # try:
    #     value = convert(to_convert, str)
    #     print(f'Type of converted value = {type(value)}')
    # except ValueError as ve:
    #     print('invalid conversion attempted')
    #     print(ve)
    # except TypeError as te:
    #     print('invalid type provided')

    # print('still going...')
    # value = convert('3.5', float)

    # list = ['a', 'b', 'c']
    # print(list)
    # pass_by_reference(list)
    # print(list)

    # valid_number = False
    # while not valid_number:
    #     number = input('Give me a number: ')
    #     try:
    #         float_number = float(number)
    #         valid_number = True
    #     except ValueError as ve:
    #         print('number is invalid')
    #         print(ve)
    #         # number = input('Give me a number: ')
            
    # print(float_number)
    # print(type(float_number))

if __name__ == '__main__':
    main()