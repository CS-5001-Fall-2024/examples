"""
Practice with for loops!
"""

def fun_with_for_loops():
    list = ['hello', 'there', 'cs', '5001', 'class']
    i = 0
    while i < len(list):
        item = list[i]		
        print(f'{i} {item}')
        i += 1

    # Iterating over a list is easier with a for loop!
    for element in list:
        # item hello
        # item there
        print(f'item: {element}')

    # Iterating over characters in a string
    name = 'Armand'
    for char in name:
        print(char)

    i = 0
    for item in list:
        print(f'{i} {item}')
        i += 1

    # Accessing the index using range()
    for i in range(len(list)):
        item = list[i]
        print(f'{i} {item}')

    # Accessing the index using enumerate

    # Using zip to iterate over two lists at once


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
    pass

def nested_loops():
    board = [
                ['x', '-', 'x'], 
                ['o', '-', '-'],
                ['-', '-', '-']
            ]

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
    fun_with_for_loops()
    # multiples_of_5(15)
    # print(count_vowels('hello'))

if __name__ == '__main__':
    main()