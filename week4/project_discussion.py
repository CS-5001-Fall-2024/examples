

result = input('Give me a number and a word: ')
# 5 bananas
# 6 gala apples
output_of_split = result.split()
if len(output_of_split) != 2:
    print('Invalid number of items in response.')
else:
    # number, word = output_of_split
    # number = int(number)
    number = int(output_of_split[0])
    word = output_of_split[1]
    if number == 5:
        print('number is 5')
    else:
        print('number is NOT 5')
