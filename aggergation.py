# In a car dealership system, you can use aggregation to represent the relationship between a "Car" class and a "Wheel" class. A car contains four wheels, and these wheels can be considered as part of the car.

# A 
class Car:
    def __init__(self, wheels):
        self.wheels = wheels

# B
class Wheel:
    pass

def main(): 
    wheell = Wheel()
    wheel2 = Wheel()
    wheel3 = Wheel()
    wheel4 = Wheel()
    car = Car([wheel1, wheel2, wheel3, wheel4])