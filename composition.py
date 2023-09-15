# : In a car simulation system, you can use composition to represent the relationship between a "Car" class and an "Engine" class. A car has a single engine, and when the car is destroyed or taken apart, the engine is destroyed as well.

# A
class Car:
    def __init__(self):
        self.engine = Engine()

# B
class Engine:
    pass

def main():
    car = Car()
