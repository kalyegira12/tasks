class appliance:
    def __init__(self, brand, power):
        self.brand = brand
        self.power = power

    def show_details(self):
      print(f"brand: {self.brand}, power: {self.power}w")    

class washingmachine(appliance):
    def __init__(self, brand, power, drum_size):
        super(). __init__(brand, power) 
        self.drum_size = drum_size

    def show_details(self):
        super(). show_details()
        print(f"brand: {self.brand}, power: {self.power}w, drum_size:{self.drum_size}")  

washingmachine1 = washingmachine("samsung", 300, 48)
washingmachine1.show_details()                   