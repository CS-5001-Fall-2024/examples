'''
Practice with recursion!
'''

def factorial_iterative(n: int) -> int:
    """
    A function that takes as a parameter an integer and returns the 
    factorial of that number.
    """
    product = 1
    while n > 0:
        product = product * n
        n = n - 1        
    return product
    

def factorial_recursive(n: int) -> int:
    """
    A function that takes as a parameter an integer and returns the 
    factorial of that number.
    This implementation does not use a loop.
    """
    if n == 1:
        return 1
    return n * factorial_recursive(n - 1)


def print_string(string: str):
    """
    Implement a recursive function that takes as a parameter 
    a str and prints the characters of the str one per 
    line *without using a loop*. 
    """
    if len(string) == 1:
        print(string)
        return
    # else:
    print(string[0])
    print_string(string[1:])


def print_string_backward(string: str):
    """
    Implement a recursive function that takes as input 
    a str and prints the characters of the str *in 
    reverse* one per line *without using a loop*. 
    """
    if len(string) == 0:
        return    
    print_string_backward(string[1:])    
    print(string[0])


def print_nums_iterative(n: int):
    """
    A function that takes as a parameter a number and prints 
    from 1 to the number (inclusive).
    """
    for i in range(1, n+1):
        print(i)

def print_nums_recursive(n: int):
    """
    Implement print_nums_iterative above without using a loop.
    There are several ways to do this. We will look at how to
    use a helper function.
    """
    # if n == 0:
    #     return
    # print_nums_recursive(n-1)
    # print(n)
    print_nums_recursive_helper(1, n)

def print_nums_recursive_helper(current: int, n: int):
    if current == n:
        print(n)
        return
    print(current)
    print_nums_recursive_helper(current+1, n)


def find_char_a(string: str, sum: int = 0) -> int:
    """
    Implement a function that returns the number of times the 
    character "a" appears in a str without using a loop. 
    You may not use the count function.
    """
    # Option 2: Tail recursion
    if len(string) == 0:
        return sum
    if string[0] == 'a':
        return find_char_a(string[1:], sum + 1)
    return find_char_a(string[1:], sum)

    # Option 1: Not tail recursion
    # if len(string) == 0:
    #     return 0
    # if string[0] == 'a':
    #     return 1 + find_char_a(string[1:])
    # return find_char_a(string [1:])



def in_english(number: int) -> str:
    """
    Write a recursive function called in_english that takes an 
    integer value as a parameter and returns a string containing 
    the digits of the number in English. For example, 
    in_english(153) would return "one five three".
    """
    pass
 

def binarysearch(list: list[int], target: int) -> bool:
     """
     Write a recursive function that returns True if the target
     exists in the list and False otherwise.
     """
     pass

     # BASE CASE???
     # list of length 0 -> return False
     # What happens if list is of length 1?
     # middle = len(list) // 2
     # if target == list[middle]:
     #    return True
     # if target < list[middle]: # go left
     #    return binary_search(list[0:middle], target)
     # if target > list[middle]: # go right
     #    return binary_search(list[middle+1:], target)




def main():
    # print(factorial_recursive(4))
    # print_string_backward('hello')
    # print_nums_recursive(5)
    print(find_char_a('abba abba'))

if __name__ == '__main__':
    main()