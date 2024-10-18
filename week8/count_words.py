def count_words(filename: str) -> dict[str, int]:
    """
    Return a dictionary that maps words in the file filename to a count of the
    number of times the word appears in the file.
    Parameter:
      filename (str)
    Return:
      dictionary: maps word -> count
    """
    pass

def top_n(mapping: dict[str, int], n: int):
    """Print the n key words from the dictionary mapping with the highest
    values.
    Parameters:
      mapping (dict[str, int]): mapping of word to count
      n (int): number of entries to print

    """
    # Option 1 using a list comprehension
    
    # Option 2 using a lambda function as a key
    pass

def lists_to_dictionary():
    names = ['Pari', 'Igor', 'Marisa']
    scores = [
        [90, 88.5, 92],
        [72, 88, 75],
        [90, 90.5, 100],
    ]

    for name, score_list in zip(names, scores):
        print(name)
        print(score_list)

def main():
    pass

if __name__ == '__main__':
    main()
