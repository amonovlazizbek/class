class Car:
    def __init__(self, brand, speed):
        self.make = brand
        self.speed = speed
        

    def get_make(self):
        return self.make

    def get_speed(self):
        return self.speed


    def drive(self):
        return f"{self.make} is moving at {self.speed} km/h"
    
car1 = Car("BMW", 120)
print(car1.drive())
