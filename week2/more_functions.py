# Write a function to calculate the average of two ints.

def get_average(num1: int, num2: int) -> float:
    average = (num1 + num2) / 2
    return average

def func1():
     print('hello')

def func2():
     print('goodbye')
     func1()

def display_message(message: str):
     print(message)
     a = 15
     print(a)
     message = 'goodbye class'
     return a, message

def main():
    a = 6
    message = 'hello, class!'
    a, message = display_message(message)
    print(a)
    # print(message)

if __name__ == '__main__':
	main()
