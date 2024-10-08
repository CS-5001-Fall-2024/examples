"""
A sample program to demonstrate the syntax of conditional statements.
"""

def main():
	# # Exercise 1
	# # if the value stored in the variable 
	# # number is less than 10 print 
	# # 'Number is small'
	# # otherwise print
	# # 'Number is not small'
	print('==================')
	print('Exercise 1')
	print('==================')	
	
	number = 15
	if number < 10:
		print('Number is small')
	else:
		print('Number is not small')


	# # Exercise 2
	# # if the value stored in the variable number
	# # is greater than 15 print
	# # 'Seems like a big number'
	# # 'Are you sure that's right?'
	# # otherwise print
	# # 'Good job!'
	# # 'You picked a good number.'
	print('\n==================')
	print('Exercise 2')
	print('==================')
	number = 5
	if number > 15:
		print('Seems like a big number')
		print('Are you sure that\'s right?')
	else:
		print('Good job!')
		print('You picked a good number')

	# # Exercise 3
	# # if the string stored in the variable animal
	# # is 'dog' print 'woof'
	# # is 'cow' print 'moo'
	# # is 'bird' print 'chirp'
	print('\n==================')
	print('Exercise 3')
	print('==================')
	animal = 'cow'
	if animal == 'dog':
		print('woof')
	elif animal == 'cow':
		print('moo')
	elif animal == 'bird':
		print('chirp')
	else:
		print('unknown animal')

	# Exercise 4
	# if the value stored in the variable first_name
	# is 'Sami' and the value stored in the variable
	# last_name is 'Rollins' print
	# 'Hey, that's my name!'
	# otherwise
	# if the value stored in the variable first_name
	# is 'Sami' print 
	# 'Cool first name...haha'
	# otherwise if the value stored in the variable last_name is 'Rollins' print
	# 'Cool last name'
	print('\n==================')
	print('Exercise 4')
	print('==================')
	first_name = 'Sonny'
	last_name = 'Rollins'

	if first_name == 'Sami' and last_name == 'Rollins':
		print('hey! that\'s my name')
	elif first_name == 'Sami':
		print('cool first name')
	else:
		print('cool last name')

	# Exercise 5
	# if the value stored in the variable user_choice is not a valid rock, paper, scissors choice print
	# 'Invalid choice'
	# otherwise print
	# 'Valid choice'
	# use only and in your solution
	print('\n==================')
	print('Exercise 5')
	print('==================')



	# Exercise 6
	# if the value stored in the variable user_choice is not a valid rock,paper, scissors choice print
	# 'Invalid choice'
	# otherwise print
	# 'Valid choice'
	# use only or and not and in your solution
	print('\n==================')
	print('Exercise 6')
	print('==================')


if __name__ == '__main__':
	main()