
# from: https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-python/#

"""
Given an expression string, write a python program to find whether a given string has balanced parentheses or not.

Examples:

Input : {{[]{()}}
Output : Unbalanced

Input : {[]{()}}
Output : Balanced

Input : [{}{})
Output : Unbalanced
"""
from stack import Stack

OPEN_CHARS = ['(', '[', '{']
CLOSE_CHARS = [')', ']', '}']


def is_balanced(parens: str) -> bool:
    # for each char in parens
    #   if open - push
    #   if close - pop and verify match
    stack = Stack(100)
    for char in parens:
        if char in OPEN_CHARS:
            # TODO: handle the case of a full stack
            stack.push(char)
        elif char in CLOSE_CHARS:        
            close = char
            if stack.size() == 0:
                return False
            item = stack.pop()
            open = item

            if OPEN_CHARS.index(open) != CLOSE_CHARS.index(close):
                return False

        else:
            return False
    if stack.size() == 0:
        return True
    return False

print(is_balanced('{{[]{()}}'))
print(is_balanced('{[]{()}}'))
print(is_balanced('[{}{})'))
print(is_balanced(''))
print(is_balanced('{[a]{()}}'))
print(is_balanced('{}]'))