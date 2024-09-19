"""
Implement a guess my number program. The computer will 
randomly generate a secret number and ask the user for 
a guess. If the user's number is the same as the secret
number a winner message will be printed. Otherwise, a 
try again message will be printed.

Phase 2:
- allow the user to keep guessing until the number is
found

Phase 3:
- keep track of the number of guesses too high and the
number of guesses too low
"""

import random
LOW = 1
HIGH = 10

def generate_secret_number() -> int:
    number = random.randint(LOW, HIGH)
    return number

def get_user_guess() -> int:
    user_guess = int(input('What is your guess? '))
    return user_guess

def compare(secret_number: int, user_guess: int) -> bool:
    """Return True if secret_number matches user_guess
    and False otherwise.
    """
    return secret_number == user_guess

def display_result(result: bool):
    if result:
        print('You guessed correctly!\nYou win!')
    else:
        print('Try again...')

def play():
    secret_number = generate_secret_number()
    # cheat for testing    
    print(f'secret number is {secret_number}')
    
    user_guess = get_user_guess()
    result = compare(secret_number, user_guess)
    # while result == False:
    # while result != True:
    while not result: 
        display_result(result)
        user_guess = get_user_guess()
        result = compare(secret_number, user_guess)
    display_result(result)

def main():
    play()

if __name__ == '__main__':
    main()