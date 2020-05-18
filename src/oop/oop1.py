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

class Vehicle():
    """
    Base class
    """

class GroundVehicle(Vehicle):
    """
    Land Vehicle Class
    """

class FlightVehicle(Vehicle):
    """
    Air Vehicle Class
    """

class Car(GroundVehicle):
    """
    Four-wheel Ground Vehicle Class
    """

class Motorcycle(GroundVehicle):
    """
    Two-wheel Ground Vehicle Class
    """

class Airplane(FlightVehicle):
    """
    Atmostpheric Vehicle Class
    """

class Starship(FlightVehicle):
    """
    Space Vehicle Class
    """
