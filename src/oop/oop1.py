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


class Vehicle(GroundVehicle):
    def __init__(self):



class FlightVehicle(Vehicle):
    def __init__(self):


class Starship(FlightVehicle, Airplane):
    def __init__(self):


class Airplane:
    def __init__(self):

class GroundVehicle:
    def __init__(self):




class Car(GroundVehicle):
    def __init__(self):

class Motorcycle(GroundVehicle):
    def __init__(self):


