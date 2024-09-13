"""
A program to prompt a user to enter a number of seconds and 
covert that to minutes.

Examples:

Enter a number of seconds: 60
You entered 60 seconds.
60 seconds is 1.0 minutes

Enter a number of seconds: 90
You entered 90 seconds.
90 seconds is 1.5 minutes

# https://docs.python.org/3/tutorial/inputoutput.html

"""
SECONDS_IN_A_MINUTE = 60
NUM_OF_SECONDS_PROMPT = 'Enter number of seconds: '

def main():
    seconds = int(input(NUM_OF_SECONDS_PROMPT))
    print(type(seconds))
    # + - * / % //
    minutes = seconds / SECONDS_IN_A_MINUTE
    print(f'You entered {seconds} seconds.')
    print(f'{seconds} is {minutes} minutes.')

if __name__ == '__main__':
	main()	