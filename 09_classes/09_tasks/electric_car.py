class Car:
    def __init__(self, make, model , year):
        #atrributes of car
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas_tank = 10
    
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
        
    
    def fill_gas_tank(self, fuel):
        if fuel >= self.gas_tank:
            self.gas_tank = fuel
            print(f"Gas tank is filled with {self.gas_tank} litres")
        else:
            print ("Fuel must be greater than the current amount of gas")

#class as attribute

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
        return range    

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
        
my_el_car = ElectricCar("Tesla","Model S",2020)
print(my_el_car.get_descriptive_name())
my_el_car.fill_gas_tank() #override the parent method without passing parameters
my_el_car.battery.describe_battery()
my_el_car.battery.get_range()
my_el_car.battery.upgrade_battery()
my_el_car.battery.get_range()





#my_new_car = Car("audi","a4",2019)
#print(my_new_car.get_descriptive_name())
#
#my_new_car.odometer_reading = 23 #directly modifying the value of odometer_reading
#
#
#my_new_car.read_odometer()
##changing attribute of class using methods
#my_new_car.update_odometer(50)
#my_new_car.read_odometer()
#
#my_used = Car("subaru","outback",2015)
#print(my_used.get_descriptive_name())
#my_used.update_odometer(23500)
##my_used.odometer_reading =12_500
#my_used.read_odometer()