from car import Car, ElectricCar
import car

my_new_car = Car('audi', 'a4', 2020)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_beetle = Car('volkswagen', 'beetle', 2020)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2020)
print(my_tesla.get_descriptive_name())

my_beetle2 = car.Car('volkswagen2', 'beetle2', 2016)
print(my_beetle2.get_descriptive_name())

my_tesla2 = car.ElectricCar('tesla2', 'roadster2', 2020)
print(my_tesla2.get_descriptive_name())
