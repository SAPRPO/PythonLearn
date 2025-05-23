from car import ElectricCar as EC #aliases

electric_car = EC('nissan', 'leaf', 2024)
print(electric_car.get_descriptive_name())
electric_car.battery.describe_battery()
electric_car.battery.get_range()