#1 Створіть клас "Транспортний засіб" та підкласи "Автомобіль", "Літак", "Корабель", наслідувані
# від "Транспортний засіб". Наповніть класи атрибутами на свій розсуд.

class Vehicle:
    speed = 70
    fuel_consumption = 10
    def __init__(self, vehicle_speed, vehicle_fuel_consumption):
        self.speed = vehicle_speed
        self.fuel_consumption = vehicle_fuel_consumption

class Car(Vehicle):
    acceleration_from_0_to_100 = 8
    def __init__(self,car_acceleration_from_0_to_100):
        self.acceleration_from_0_to_100 = car_acceleration_from_0_to_100
    def inf_car(self):
        return f"This car accelerates from 0 to 100 in {self.acceleration_from_0_to_100} seconds"
class Airplane(Vehicle):
    load_capacity = 100
    def __init__(self,airplane_load_capacity):
        self.load_capacity = airplane_load_capacity
    def inf_airplane(self):
        return f"This aircraft can carry {self.load_capacity} kg of cargo"
class Ship(Vehicle):
    storm_resistance = 3
    def __init__(self,ship_storm_resistance):
        self.storm_resistance = ship_storm_resistance
    def inf_ship(self):
        return f"This ship can withstand curtains up to {self.storm_resistance} balls"

#2 Створіть обʼєкти класів "Автомобіль", "Літак", "Корабель".

car1 = Car(car_acceleration_from_0_to_100 = 4)
print(car1.inf_car())

airplane1 = Airplane(airplane_load_capacity = 50)
print(airplane1.inf_airplane())

ship1 = Ship(ship_storm_resistance = 5)
print(ship1.inf_ship())