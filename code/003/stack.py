# Description: Stack implementation using list
data = [] # empty list
data.append(5) # push 5 - add 5 to the top
print(data[len(data) - 1]) # 5 - peel the top element
element = data.pop() # pop 5 - remove the top element
print(element) # 5 - print the removed element