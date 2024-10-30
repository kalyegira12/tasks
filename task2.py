# Defining the first parent class Camera
class Camera:
    def take_photo(self):
        print("Taking a photo..")

# Define the second parent class Phone
class Phone:
    def make_call(self):
        print("Making a phone call..")

# Define the child class Smartphone, inheriting from both Camera and Phone
class Smartphone(Camera, Phone):
    pass

# Create an instance of the Smartphone class and demonstrate calling both methods
smartphone = Smartphone()
smartphone.take_photo()
smartphone.make_call()
