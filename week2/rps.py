"""Rock / Paper / Scissors Game
"""

# USER = 1
# COMPUTER = -1
# TIE = 0

# if winner == USER:
#     print('User wins!')


# if computer_choice == 'rock' and user_choice == 'paper':
#     return USER

# def is_choice_valid(user_choice: str) -> bool:
#     if (user_choice == 'rock' 
#         or user_choice == 'paper' 
#         or user_choice == 'scissors'):
#         return True
#     else:
#         return False

# def is_choice_valid(user_choice: str) -> bool:
#     if (user_choice == 'rock' 
#         or user_choice == 'paper' 
#         or user_choice == 'scissors'):
#         return True
#     return False

def is_choice_valid(user_choice: str) -> bool:
    return (user_choice == 'rock' 
        or user_choice == 'paper' 
        or user_choice == 'scissors')

def is_choice_invalid(user_choice: str) -> bool:
    return (user_choice != 'rock' 
            and user_choice != 'paper' 
            and user_choice != 'scissors')

# user_choice = 'rock'
# print(user_choice == 'paper' or user_choice == 'rock')

# print(is_choice_valid('paper'))
