from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def find_car(self): pass


class LuxuryCar(Vehicle):
    def find_car(self):
        print("find luxury car ... ")


class PopularCar(Vehicle):
    def find_car(self):
        print("find popular car ... ")


class ElectricCar(Vehicle):
    def find_car(self):
        print("find electric car ... ")


class FordCar(Vehicle):

    @staticmethod
    def get_car(name):
        return eval(f"{name}Car")()


if __name__ == '__main__':
    car_type = input("What type of car would you like to select ? [Luxury, Popular, Electric]")
    car = FordCar.get_car(car_type)

    print("Type of : ", type(car).__name__, "Instance : ", car)
