# Description: Stack implementation using list
data = [] # empty list
data.append(5) # push 5 - add 5 to the top
print(data[len(data) - 1]) # 5 - peel the top element
element = data.pop() # pop 5 - remove the top element
print(element) # 5 - print the removed element

# Description: Stack implementation using deque
class Stack:
    def __init__(self): # constructor
        self.data = [] # empty list

    def push(self, value): # push method
        self.data.append(value) # add value to the top

    def peek(self): # peek method
        return self.data[len(self.data) - 1] # return the top element
    
    def pop(self): # pop method
        return self.data.pop() # remove the top element
    

# Usage
# Create a stack
stack = Stack()
# Push 5
stack.push(5)   
# Peek the top element
print(stack.peek()) # 5
# Pop 5
print(stack.pop()) # 5

