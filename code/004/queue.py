from collections import deque # import deque from collections

# Description: queue implementation using list
data = [] # empty list
data.append(5) # enqueue 5 - add 5 to the rear
print(data[0]) # 5 - peek the front element
element = data.pop(0) # dequeue 5 - remove the front element
print(element) # 5 - print the removed element

data2 = deque() # empty deque
data2.append(5) # enqueue 5 - add 5 to the rear
print(data2[0]) # 5 - peek the front element
element = data2.popleft() # dequeue 5 - remove the front element
print(element) # 5 - print the removed element
