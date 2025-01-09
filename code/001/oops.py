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
