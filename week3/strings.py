"""
Practice with strings!
"""

def fun_with_strings():
    """
    What can you do with a string?!
    https://docs.python.org/3/library/stdtypes.html#string-methods
    """
    word = 'hello, class!'	
    # print(word[2])


    # Strings are immutable!	
    # Accessing individual characters
    # print(word.center(100))
    # word[2] = 'X' # CANNOT DO THIS

    # updated_word = word.replace('l', 'X')
    # print(updated_word)

    # word = word.replace('l', 'X')
    # print(word)

    # Calling string methods -- like replace!


    # Slicing strings
    print(word[4:])


def reverse(phrase: str) -> str:
    """
    A function to reverse the string passed as input.
    """
    # return phrase[::-1]

    result = ''
    i = len(phrase) - 1
    while i >= 0:
        result = result + phrase[i]
        i = i - 1
    return result

def is_palindrome(word: str) -> bool:
    """
    A palindrome is a word that is the same forward
    and backward. Examples are madam, racecar, and deed.
    This function takes as input a word and returns True
    if the word is a palindrome and False otherwise.
    You may assume that the string does not contain spaces.
    Consider two different approaches to implementing 
    this function.
    """
    # return word == word[::-1]
    # return word == reverse(word)
    start = 0 
    end = len(word) - 1
    while start < end: 
        # are the chars at start and end the same?
        # if not -- return False
        if word[start] != word[end]:
            return False
        start = start + 1
        end = end - 1
    return True

def main():
    print(is_palindrome('racecar'))
    print(is_palindrome('deed'))
    print(is_palindrome('hello'))


    # fun_with_strings()
    # word = 'hello'
    # reversed_word = reverse(word)
    # print(reversed_word)
    # first_name = 'Sami'
    # last_name = 'Rollins'
    # full_name = first_name + ' ' + last_name
    # user_name = first_name[0] + last_name
    # print(user_name)


if __name__ == '__main__':
    main()