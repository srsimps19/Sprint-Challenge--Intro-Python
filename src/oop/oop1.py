# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:
    def __init__(self):
        #this is the base class
        pass
        

class GroundVehicle(Vehicle):
    def __init__(self):
        super().__init__()
        #the base class is vehicle
        pass

class Car(GroundVehicle):
    def __init__(self):
        super().__init__()
        #the base class is ground vehicle
        pass

class Motorcycle(GroundVehicle):
    def __init__(self):
        super().__init__()
        #the base class is ground vehicle
        pass


class FlightVehicle(Vehicle):
    def __init__(self):
        super().__init__()
        #the base class is vehicle
        pass

class Starship(FlightVehicle):
    def __init__(self):
        super().__init__()
        #the base class is flight vehicle
        pass

class Airplane(FlightVehicle):
    def __init__(self):
        super().__init__()
        #the base class is flight vehicle
        pass