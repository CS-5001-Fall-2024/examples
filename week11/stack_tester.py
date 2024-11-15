from stack import Stack

stack1 = Stack(10)
stack1.push(1)
stack1.push(2)
print(stack1.pop())
stack1.push(3)
stack1.push(4)
print(stack1.pop())
print(stack1.pop())
stack1.push(5)
stack1.debug()

stack2 = Stack(2)
stack2.push('a')
stack2.push('b')
stack2.push('c')
stack1.debug()
stack2.debug()
