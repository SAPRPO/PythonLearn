class Car:
    def __init__(self, make, model , year):
        #atrributes of car
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self,mileage):
        if mileage>= self.odometer_reading:
            self.odometer_reading = mileage
            
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        self.odometer_reading+=miles

class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery")

    def get_range(self):
        if self.battery_size == 40:
            range = 150
            
        elif self.battery_size == 65:
            range = 225
        #return range 
        print(f"This car can go about {range} miles on a full charge")   

    def upgrade_battery(self):
        self.battery_size = 65

        print(f"Battery upgraded. This car can go about {self.get_range()} miles on a full charge. Battery size = {self.battery_size}")
       
    
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year) #конструктор базового  класса (суперкласса). Потомок  -подкласс
        #attributes of ElectricCar
        #self.battery_size=40
        self.battery = Battery()

    
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        
        print("This car doesn't need a gas tank!")