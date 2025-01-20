# Description: queue implementation using list
data = [] # empty list
data.append(5) # enqueue 5 - add 5 to the rear
print(data[0]) # 5 - peek the front element
element = data.pop(0) # dequeue 5 - remove the front element
print(element) # 5 - print the removed element
