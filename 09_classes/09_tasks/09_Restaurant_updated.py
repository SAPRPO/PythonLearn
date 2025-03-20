class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cousine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print (f"Restaurant Name: {self.restaurant_name}")
        print (f"Cuisine Type: {self.cousine_type}")
    
    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is now open!")

my_restaurant = Restaurant("Pizza Hut", "Pizza")

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.number_served = 10
print(f"Number of customers served: {my_restaurant.number_served}")

