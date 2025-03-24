class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cousine_type = cuisine_type
        self.numberserved = 0
    
    def describe_restaurant(self):
        print (f"Restaurant Name: {self.restaurant_name}")
        print (f"Cuisine Type: {self.cousine_type}")
    
    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is now open!")
    
    def set_number_served(self, visitors):
        self.numberserved = visitors
        print(f"Number of served visitors: {self.numberserved}")

    def increment_number_served(self, visitors):
        #if visitors >= self.numberserved:
        #    print(f"current visitors: {visitors}")
            self.numberserved += visitors
            print(f"current visitors: {self.numberserved}")
        #else:
        #    print(f"Error! Number of visitors can't be less then served in day")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavours):
          super().__init__(restaurant_name, cuisine_type)
          self.flavours =flavours
    
    def showFlavour(self):
         print(f"Your ingredients: ")
         for f in self.flavours:
              print(f)




my_restaurant = Restaurant("Pizza Hut", "Pizza")

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

restaurant = Restaurant("Irish Pub", "Pub")
served = restaurant.numberserved = 10

print(served)

restaurant.set_number_served(20)

restaurant.increment_number_served(10)


#IceCreamStand
ice = IceCreamStand('Baskin Robins', 'Ice cream', ['cherry', 'strawberry', 'apple'])
ice.showFlavour()