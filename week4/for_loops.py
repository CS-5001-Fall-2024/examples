"""
Practice with for loops!
"""

def fun_with_for_loops():
    list = ['hello', 'there', 'cs', '5001', 'class']
    # i = 0
    # while i < len(list):
    #     item = list[i]		
    #     print(f'{i} {item}')
    #     i += 1

    # # Iterating over a list is easier with a for loop!
    # for element in list:
    #     # item hello
    #     # item there
    #     print(f'item: {element}')

    # # Iterating over characters in a string
    # name = 'Armand'
    # for char in name:
    #     print(char)

    # i = 0
    # for item in list:
    #     print(f'{i} {item}')
    #     i += 1

    # # Accessing the index using range()
    # for i in range(len(list)):
    #     item = list[i]
    #     print(f'{i} {item}')

    # Accessing the index using enumerate
    # for item in enumerate(list):
    #     print(f'index: {item[0]} - value: {item[1]}')

    # Using zip to iterate over two lists at once
    list1 = ['a', 'b', 'c']
    list2 = ['d', 'e', 'f', 'g']

    for item in zip(list1, list2):
        print(item)


def multiples_of_5(number: int):
    """
    A function that takes as a parameter a positive integer and
    uses a for loop to print the multiples of 5 that are 
    less than or equal to the number that was entered.
    """
    # for i in range(5, number+1, 5):
    #     print(i)
    for i in range(number+1):
        if i % 5 == 0:
            print(i)


def is_valid(list) -> bool:
    # for item in list:
    #     if type(item) != str:
    #         return False        
    # return True

    result = True
    for item in list:
        if type(item) != str or len(item) == 0:
            result = False
            break
    return result

def validate_lists(list1, list2) -> bool:
    if is_valid(list1) and is_valid(list2) and len(list1) == len(list2):
        return True
    return False

def generate_user_names(first_names: list[str], 
    last_names: list[str]) -> list[str]:
    """
    A function that takes as input a list of strings
    representing first names and a list of strings representing
    last names and returns a list of usernames where the ith username
    is the first initial of the first name stored at the ith position
    of the first_names list concatenated with the first 7 characters 
    of the last name stored at the ith position of the last_names
    list.
    """
    if not validate_lists(first_names, last_names):
        return []
    
    result = []
    # zip to match up first/last
    for item in zip(first_names, last_names):
        # print(item)
        first = item[0]
        last = item [1]

        # first char from item[0]
        # first seven chars from item[1]
        user_name = first[0] + last[0:7]
        user_name = user_name.lower()
        # user_name = item[0][0]
        result.append(user_name)
        # print(user_name)
    return result

def check_board(board):
    # check 8 cases
    if ((board[0][0] == board[0][1] == board[0][2])
         and (board[0][0] == 'x' or board[0][0] == 'o')
        ):
        # win on first row
        return True
    elif ((board[0][1] == board[1][1] == board[2][1])
          and(board[0][1] == 'x' or board[0][1] == 'o')): 
        # win in second column
        return True


def nested_loops():
    board = [
                ['x', '-', 'x'], 
                ['o', '-', '-'],
                ['-', '-', '-']
            ]
    board[0][1] = 'o'
    # print(board)

    
    # for row in board:
    #     # row -- type is list
    #     board_str = ''
    #     for char in row:
    #         board_str += char
    #     print(board_str)
    
    # board_str += '\n'

    board_str = ''
    for row in board:
        # row -- type is list
        for char in row:
            board_str += char
        board_str += '\n'    
    print(board_str)


def gradebook():
    pass

VOWELS = ('a', 'e', 'i', 'o', 'u')

def is_vowel(letter: str) -> bool:
    return letter in VOWELS
    # return (letter == 'a' 
    #         or letter == 'e' 
    #         or letter == 'i' 
    #         or letter == 'o' 
    #         or letter == 'u')

def count_vowels(sentence: str) -> int:
    """
    A function that takes as input a string and returns the number
    of vowels (a, e, i, o, u) that are found in the sentence.
    """
    count = 0
    for letter in sentence:
        if is_vowel(letter):
            count += 1
    return count

def main():
    # fun_with_for_loops()
    # multiples_of_5(15)
    # print(count_vowels('hello'))

    first_names = ['Edwin', 'Aaron', 'Amber']
    last_names = ['Jones', 'Smith', 'SaberiGoetz']

    # last_names = ['Jones', 'Smith', 'SaberiGoetz', True, 'Rollins', 'Berket']
    # i = 0 
    # while True:
    #     if i >= len(last_names):
    #         break
    #     print(last_names[i])
    #     i += 1


    # print(is_valid(last_names))

    # user_names = generate_user_names(first_names, last_names)
    # print(user_names)

    nested_loops()


if __name__ == '__main__':
    main()