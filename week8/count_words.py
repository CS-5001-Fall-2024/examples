def count_words(filename: str) -> dict[str, int]:
    """
    Return a dictionary that maps words in the file filename to a count of the
    number of times the word appears in the file.
    Parameter:
      filename (str)
    Return:
      dictionary: maps word -> count
    """
    # open the file -- fnf?
    # for each line
    #   split the line
    #   for each word in splitline
    #     if not in the dictionary: add with a value of 1
    #     else increment the value associated with the key by 1

    word_to_count = {}
    with open(filename, 'r') as input_file:
        for line in input_file:
            splitline = line.split()
            for word in splitline:
                word = word.lower()
                if word not in word_to_count:
                    word_to_count[word] = 1
                else:
                    word_to_count[word] = word_to_count[word] + 1

    return word_to_count


def top_n(mapping: dict[str, int], n: int):
    """Print the n key words from the dictionary mapping with the highest
    values.
    Parameters:
      mapping (dict[str, int]): mapping of word to count
      n (int): number of entries to print

    """
    # sort the values and find the keys associated with the first n

    # compare values to see which is highest

    # mapping.keys()
    # mapping.values()
    # mapping.items()
    # First cut to find just the top 1 item
    # max_item = None
    # for item in mapping.items():
    #     if (not max_item or item[1] > max_item[1]):
    #         max_item = item
    # print(max_item)

    # print(sorted(mapping.items()))
    # Option 1 using a list comprehension
    # mapping = {}    
    # items = [(value, key) for key, value in mapping.items()]
    # sorted_items = sorted(items, reverse=True)
    # print(sorted_items)
    # result = sorted_items[:n]
    # print(result)
    # for value, key in result:
    #     print(key)

    # Option 2 using a lambda function as a key
    result = sorted(mapping.items(), key=lambda x:x[0]+str(x[1]), reverse=True)
    print(result)

def get_average_for_student(student_name, data):
    if student_name not in data:
        return -1

    # Algorithm for dictionary approach
    # use name to get value (scores list) from data
    scores = data[student_name]
    # sum scores in the list and divide by length of list
    avg = sum(scores) / len(scores)
    return avg

    # Algorithm for list of lists approach
    # find index of student_name in names
    # get the scores list from scores at position index
    # sum scores in the list and divide by length of list


def lists_to_dictionary():
    # maps key -> value
    data = {
        'Logan': [100, 100, 100],
        'Ashley': [99, 99, 100]
    }
    data['Pari'] = [90, 88.5, 92]
    data['Ashley'] = [72, 88, 75]
    data['Marisa'] = [90, 90.5, 100]

    return data

    # for item in data.values():
    #     print(item)

    # Option 1: parallel lists
    # names = ['Pari', 'Igor', 'Marisa']
    # scores = [
    #     [90, 88.5, 92],
    #     [72, 88, 75],
    #     [90, 90.5, 100],
    # ]

    # for name, score_list in zip(names, scores):
    #     print(name)
    #     print(score_list)


def main():
    # data = lists_to_dictionary()
    # result = get_average_for_student('Edwin', data)
    # print(result)
    result = count_words('cat.txt')
    print(result)
    top_n(result, 2)
    # print(result['the'])


if __name__ == '__main__':
    main()
