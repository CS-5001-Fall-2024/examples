def find_permutations(word: str) -> list[str]:
    if len(word) == 1:
        return [word]
    permutations = []
    for i in range(len(word)):
        smaller_word = word[:i]+word[i+1:]        
        results = find_permutations(smaller_word)
        for result in results:
            permutations.append(word[i] + result)
    return permutations

print(find_permutations('handy'))

def check_wordle(secret: str, guess: str, result = 0) -> int:
    
    if len(secret) != len(guess):
        raise Exception('secret and guess must be the same length')

    if len(secret) == 0 and len(guess) == 0:
        return result
    
    # recursive call
    if secret[0] == guess[0]:
        return check_wordle(secret[1:], guess[1:], result + 1)
    return check_wordle(secret[1:], guess[1:], result)


"""
 Write a recursive function check_wordle that takes as a parameter a wordle word and a guess and returns the number of green letters -- that is, the number of letters that are the same letter in the same position in both the wordle word and the guess. For full credit this function must be recursive.
"""
# def check_wordle(secret: str, guess: str) -> int:
    
#     if len(secret) != len(guess):
#         raise Exception('secret and guess must be the same length')

#     if len(secret) == 0 and len(guess) == 0:
#         return 0

#     # if len(secret) == 1 and len(guess) == 1:
#     #     if secret == guess:
#     #         return 1
#     #     return 0
    
#     # recursive call
#     if secret[0] == guess[0]:
#         return 1 + check_wordle(secret[1:], guess[1:])
#     return check_wordle(secret[1:], guess[1:])

# print(check_wordle('heart', 'check'))
# print(check_wordle('heart', 'heard'))
# print(check_wordle('heart', 'start'))
# print(check_wordle('', ''))
# print(check_wordle('cat', ''))


'''
ChatGPT solve and check_rows solutions
'''

def solve(board):
    # Find the next empty square (represented by 0)
    empty = find_empty(board)
    if not empty:
        return True  # No empty cells left, puzzle solved!

    row, col = empty
    candidates = candidate_values(board, row, col)

    for num in candidates:
        board[row][col] = num  # Try placing the number
        if solve(board):  # Recursively attempt to solve with this number
            return True
        board[row][col] = 0  # Backtrack

    return False  # If no valid number works, return False (unsolvable)


def check_rows(board):
    # Iterate over each row in the board
    for row in board:
        # Filter out zeros (empty cells) and check if the row contains exactly
        # the numbers 1 through 9

        # for num in row: 
        #     if num != 0:
        #         row_values.append(num)

        dictionary = {
            1: 'a', 
            2: 'b', 
            3: 'c'
        }

        my_list = [(value, key) for key, value in dictionary.items()]
        # [('a', 1), ('b', 2), ('c', 3)]


        row_values = [num for num in row if num != 0]
        if len(row_values) != len(set(row_values)):  # If there are duplicates
            return False
        if sorted(row_values) != list(range(1, 10)):  # Ensure all numbers 1-9 are present
            return False
    return True
