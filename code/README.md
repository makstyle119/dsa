#  Data Structures and Algorithm

always remember data structure and algorithm are both connected 

## Folder Structure:

```
📂 code
├── 📂 001
|   ├── 📄 oops.py
└── 📄 README.md
```

## Code Explaining

- code/001/oops.py
```
from enum import Enum  # Import Enum for creating enumerations

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
class Camera:
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