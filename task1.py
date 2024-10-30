#creating class device as the parent class
class device:
    def __init__(self, brand, model): #defining the brand and the model that are part of the class of device
        self.brand = brand
        self.model = model
    def show_info(self):
        print(f"brand: {self.brand}, model: {self.model}")    

#creating the child class from the device class which is the parent class        
class Smartphone(device):
    def __init__(self, brand, model, storage_capacity):#defining the things that fall under the device class
        super(). __init__(brand, model)
        self.storage_capacity = storage_capacity 

    def show_info(self):# overriding the show_info to add storage_capacity
        print(f"brand: {self.brand}, model: {self.model}, storage_capacity: {self.storage_capacity}")

#demostrating an object by using the show_info() method
Smartphone = Smartphone("Andriod", "2024", "245")
Smartphone.show_info()     