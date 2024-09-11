"""
A python program to demonstrate how to use functions.
"""

def welcome():
	"""Exercise 1: 
	A function to print a multi-line welcome message.
	You can print this documentation using 
	print(welcome.__doc__)
	"""	
	print('Welcome!')
	print('Glad to have you in 5001 class.')

def greet_by_name(name: str):
	"""Exercise 2:
	A function to greet a user by name.
	Parameters
	name: str
		name of the user
	"""
	print(f'Hello, {name}')

def get_greeting() -> str:
	"""Exercise 3:
	A function to get a specific greeting from the user.
	Returns:
	str 
		greeting provided by the user
	"""
	greeting = input('What is your greeting? ')
	return greeting

def welcome_by_name_with_greeting(name: str, greeting: str=None):
	"""Exercise 4:
	A function to welcome a user by name with a 
	specific greeting.
	Parameters:
	name: str
		name of the user
	greeting: str
		greeting to use
	"""
	print(f'{greeting}, {name}!')

def main():
	returned_greeting = get_greeting()	
	welcome_by_name_with_greeting('Amber', returned_greeting)
	welcome_by_name_with_greeting('Ashley')

	# greet_by_name('Edwin')
	# greet_by_name('Logan')

	# print(welcome.__doc__)
	# call functions!
	# welcome()
	# welcome()
	# welcome()

if __name__ == '__main__':
	main()