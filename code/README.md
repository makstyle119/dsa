#  Data Structures and Algorithm

always remember data structure and algorithm are both connected 

## Folder Structure:

```
📂 code
├── 📂 001
|   ├── 📄 oops.py
├── 📂 002
|   ├── 📄 linked_list.py
├── 📂 003
|   ├── 📄 stack.py
├── 📂 004
|   ├── 📄 queue.py
├── 📂 005
|   ├── 📄 hashTable.py
├── 📂 006
|   ├── 📄 sets.py
└── 📄 README.md
```

## Code Explaining

- code/001/oops.py
```python
from enum import Enum  # Import Enum for creating enumerations

# Base class representing a security device
class Security_Device:
    def __init__(self, active):
        # Initializes the Security_Device object with an active status
        self.active = active
    
    def reset(self):
        # Resets the security device to the active state
        self.active = True

# Subclass representing a sensor that inherits from Security_Device
class Sensor(Security_Device):
    def __init__(self, silent, distance):
        # Since this class is inheriting, we need to call the parent constructor explicitly if we use new attributes
        super().__init__(True)  # Call the parent class constructor with a default active state
        self.silent = silent  # Whether the sensor is silent
        self.distance = distance  # The range of the sensor

# Create an instance of Security_Device
security_device = Security_Device(True)

# Create an instance of Sensor
sensor = Sensor(True, 10)

# Call the reset method from the parent class to reset the sensor's active state
sensor.reset()
print(sensor.active)  # Print the active state of the sensor

# Print the type of the sensor object
print(type(sensor))

# Check if the sensor object is an instance of the Security_Device class
print(isinstance(sensor, Security_Device))

# Check if the Sensor class is a subclass of Security_Device
print(issubclass(Sensor, Security_Device))

# Class representing a camera's position with pan, tilt, and zoom attributes
class Position:
    def __init__(self, pan, tilt, zoom):
        # The __init__ method initializes the Position object with specific pan, tilt, and zoom values
        self.pan = pan  # Pan angle of the camera
        self.tilt = tilt  # Tilt angle of the camera
        self.zoom = zoom  # Zoom level of the camera

    def log(self):
        # The log method prints the current position details for debugging or monitoring
        print(f"Pan: {self.pan}, Tilt: {self.tilt}, Zoom: {self.zoom}")

# Class representing a camera with a serial number, position, and type
class Camera (Security_Device):
    def __init__(self, serial_number, position, camera_type):
        # The __init__ method initializes the Camera object with specific attributes
        self.serial_number = serial_number  # Unique identifier for the camera
        self.position = position  # Position object containing pan, tilt, and zoom values
        self.camera_type = camera_type  # Type of camera (e.g., PTZ, Fixed, Dome)

    def log(self):
        # The log method prints the camera details, including its position and type
        print(f"Serial Number: {self.serial_number}")
        self.position.log()  # Log the position details
        print(f"Camera Type: {self.camera_type}")

    # Enumeration defining different types of cameras
    class CameraType(Enum):
        PTZ = 1  # Pan-Tilt-Zoom camera
        FIXED = 2  # Fixed camera
        DOME = 3  # Dome camera

# Create a Camera object with specific attributes
c = Camera("1234", Position(10, 20, 30), Camera.CameraType.PTZ)

# Log the details of the camera
c.log()
```

- code/002/linked_list.py
```python
class Node:
    """
    Represents a single node in the linked list.
    """
    def __init__(self, data):
        """
        Initializes a new node with the given data.

        Args:
            data: The data to be stored in the node.
        """
        self.data = data
        self.next = None 

class LinkedList:
    """
    Represents a linked list data structure.
    """
    def __init__(self):
        """
        Initializes an empty linked list.
        """
        self.head = None

    def append(self, data):
        """
        Adds a new node to the end of the linked list.

        Args:
            data: The data to be stored in the new node.
        """
        new_node = Node(data) 

        if self.head is None:  # If the list is empty
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    def print_list(self):
        """
        Prints the data of all nodes in the linked list.
        """
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

# Example usage
if __name__ == "__main__":
    my_list = LinkedList()
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)
    my_list.append(40)
    my_list.print_list()  # Output: 10 20 30 40
```

- code/003/stack.py
```python
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
```

- code/004/queue.py
```python
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
```

- code/005/hashTable.py
```python
# hash table implementation
data = {}
data['a'] = 1 # key-value pair
data['b'] = 2 
data['c'] = 3
print(data) # {'a': 1, 'b': 2, 'c': 3}
print(data['a']) # 1
print(data['b'])
print(data['c'])
print(data.keys()) # dict_keys(['a', 'b', 'c']) - dict_keys is a view object
print(data.values()) # dict_values([1, 2, 3]) - dict_values is a view object
print(data.items()) # dict_items([('a', 1), ('b', 2), ('c', 3)]) - dict_items is a view object
```

- code/006/sets.py
```python
# sets implementation
colors = {'red', 'green', 'blue'}
colors.add('yellow')
print(colors) # {'red', 'green', 'blue', 'yellow'}
colors.remove('red') # remove element
print(colors) # {'green', 'blue', 'yellow'}
print('red' in colors) # False
print('green' in colors) # True
colors.clear() # remove all elements
print(colors) # set()
# set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b) # union {1, 2, 3, 4, 5, 6}
print(a & b) # intersection {3, 4}
print(a - b) # difference {1, 2}
print(a ^ b) # symmetric difference {1, 2, 5, 6}
# set comprehension
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a) # {'r', 'd'}
# frozenset
a = frozenset([1, 2, 3, 4]) # immutable set
print(a) # frozenset({1, 2, 3, 4})
# a.add(5) # AttributeError: 'frozenset' object has no attribute 'add'
# a.remove(1) # AttributeError: 'frozenset' object has no attribute 'remove'
# a.clear() # AttributeError: 'frozenset' object has no attribute 'clear'
b = frozenset([3, 4, 5, 6])
print(a | b) # frozenset({1, 2, 3, 4, 5, 6})
print(a & b) # frozenset({3, 4})
print(a - b) # frozenset({1, 2})
print(a ^ b) # frozenset({1, 2, 5, 6})
# a |= b # TypeError: unsupported operand type(s) for |=: 'frozenset' and 'frozenset'
# a &= b # TypeError: unsupported operand type(s) for &=: 'frozenset' and 'frozenset'
# a -= b # TypeError: unsupported operand type(s) for -=: 'frozenset' and 'frozenset'
# a ^= b # TypeError: unsupported operand type(s) for ^=: 'frozenset' and 'frozenset'
# a = {x for x in 'abracadabra' if x not in 'abc'} # TypeError: unhashable type: 'set'
# a = frozenset({x for x in 'abracadabra' if x not in 'abc'}) # TypeError: unhashable type: 'set'
# frozenset comprehension is not possible
```
