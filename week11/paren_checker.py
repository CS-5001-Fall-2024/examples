
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

