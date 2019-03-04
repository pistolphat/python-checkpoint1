# #1: Define a Vehicle class with the following properties and methods: 
# - `vehicle_type` 
# - `wheel_count`
# - `name` 
# - `cost` 
# - `colors` 
# - `vehicle_brand` 
# - `mpg`, a 'dict', with the following properties:
#     - `city`
#     - `highway` 
#     - `combined` 
# - `get_vehicle_type` should return the `vehicle_type`
# - `get_vehicle_brand` should return the classes `vehicle_brand`
# - `get_vehicle_drive` if the `wheel_count` for that class is "no wheels!" then
#     it should return "no wheels send it back to the shop" otherwise it should
#     return "I have "  + self.wheel_count  + " wheel drive"
#
# Your Vehicle class should take one argument (a `dict`) with the above
# attributes. Define the properties on the class from the dict that is passed in.



class Vehicle:
  def __init__(self, dict):
    self.dict = dict
    self.vehicle_type = dict['vehicle_type']
    self.wheel_count = dict['wheel_count']
    self.name = dict['name']
    self.cost = dict['cost']
    self.colors = dict['colors']
    self.vehicle_brand = dict['vehicle_brand']
    self.mpg = dict['mpg']


# #2: Create a Motorcycle class that inherits from the Vehicle class and has the
# following properties and methods:
# - property: `wheel_count` defaults to "no wheels!"
# - method: `pop_wheelie` if `wheel_count` is not equal to 2 then it should be False,
#       otherwise return "......pop!"

class Motorcycle(Vehicle):
  def __init___(self):
    super().__init__(self, dict)

  def pop_wheelie(self):
    if 

  
# #3: Define a Car class that inherits from the vehicle class with the following attributes and methods:
# - property: `wheel_count` defaults to 4
# - method: `can_drive` that should return 'Vrrooooom Vroooom'

class Car(Vehicle):
  def __init__(self):
    super().__init__(self, dict)
  
  def can_drive(self):
    print('Vrroooom Vroooom')


# #4: Define a Truck class that inherits from the vehicle class with the following attributes and methods:
# - property: `wheel_count` defaults to "no wheels!"
# - method: `rev_engine` that should return 'revvvvvreeeev'

class Truck(Vehicle):
  def __init__(self):
    super().__init__(self,dict)
  
  def rev_engine(self):
    print('revvvvvreeeev')



# Commit when you finish working on these questions!