# WRITE YOUR SOLUTION HERE:
class Car:
    def __init__(self):
        self.__tank = 0
        self.__odo = 0  
    
    def fill_up(self):
        self.__tank = 60
    
    def drive(self, km: int):
        if self.__tank > km:
            self.__odo += km
            self.__tank -= km
        else:
            self.__odo += self.__tank
            self.__tank = 0
    
    def __str__(self):
        return f"Car: odometer reading {self.__odo} km, petrol remaining {self.__tank} litres"
    
# Example Usage
car = Car()
print(car)
car.fill_up()
print(car)
car.drive(20)
print(car)
car.drive(50)
print(car)
car.drive(10)
print(car)
car.fill_up()
car.fill_up()
print(car)