#  Data Structures and Algorithm

always remember data structure and algorithm are both connected 

## Folder Structure:

```
📂 code
├── 📂 001
|   ├── 📄 oops.py
├── 📂 002
|   ├── 📄 linked_list.py
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
```
