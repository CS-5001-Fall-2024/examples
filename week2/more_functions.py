# Write a function to calculate the average of two ints.

def get_average(num1: int, num2: int) -> float:
    average = (num1 + num2) / 2
    return average

def func1():
     print('hello')

def func2():
     print('goodbye')
     func1()

def main():
    # print(get_average(10, 20))
    func2()

if __name__ == '__main__':
	main()
