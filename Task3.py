class vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type
        

    def start(self):
      print(f"The {self.vehicle_type} is going to start")

class car(vehicle):
   def __init__(self, vehicle_type, number_of_doors):
      super(). __init__(vehicle_type)
      self.number_of_doors = number_of_doors

   def show_doors(self):
      print(f"this {self.vehicle_type} has {self.number_of_doors}")

class electric_car(car):
   def __init__(self, vehicle_type, number_of_doors, battery_capacity):
      super(). __init__(vehicle_type, number_of_doors)
      self.battery_capacity = battery_capacity

   def show_battery(self):
      print(f"This specific car has a battery capacity of {self.battery_capacity}watts")


Tesla = electric_car("Electric Car", 4, 75)
Tesla.start()          
Tesla.show_doors()      
Tesla.show_battery() 

      
      
                     