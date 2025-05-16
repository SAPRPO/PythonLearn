from car import Car

my_new_car = Car("audi","a4",2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23 #directly modifying the value of odometer_reading


my_new_car.read_odometer()
#changing attribute of class using methods
my_new_car.update_odometer(50)
my_new_car.read_odometer()

my_used = Car("subaru","outback",2015)
print(my_used.get_descriptive_name())
my_used.update_odometer(23500)
#my_used.odometer_reading =12_500
my_used.read_odometer()