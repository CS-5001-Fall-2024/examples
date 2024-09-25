"""
Practice with lists!
"""
def fun_with_lists():
    """
    What can you do with a list?!
    """
    # Lists are mutable!
    # Creating a list
    words = ['one', 'two', 'three']
    print(len(words))

    # Accessing elements of a list
    print(words[2])

    # Modifying lists
    words[1] = 'HELLO'
    print(words)

    # Appending to a list
    words.append('four')
    print(words)

    # Lists of mixed types
    words.append(45)
    print(words)

    words.append([3, 4, 5])
    print(words[5][2])
    # Slicing a list	
    print(words[2:4])

def list_to_string(list_of_string: list[str]) -> str:
    """
    A function that takes a list of strings and
    combines them into a single string with 
    spaces between each word. Returns the string.		
    """
    pass

def greater_than_100(values: list[int]) -> int:
    """
    A function that takes as input a list of ints
    and returns the number of ints in the list that
    are greater than 100.
    values = [1, 2, 3, 4] ==> 0
    values = [1, 200, 300, 4] ==> 2	
    """
    count = 0
    for item in values:
        if item > 100:
            count += 1
            # count = count + 1
    return count
    # count = 0
    # i = 0
    # while i < len(values):
    #     item = values[i]
    #     if item > 100:
    #     # if values[i] > 100:
    #     #     count += 1
    #     i = i + 1
    # return count
    

def main():
    # print(greater_than_100([1, 2, 3, 4]))
    # print(greater_than_100([1, 200, 300, 4]))
    # fun_with_lists()
    
    list = [1, 2, 3]
    for number in list:
        print(number)


if __name__ == '__main__':
    main()