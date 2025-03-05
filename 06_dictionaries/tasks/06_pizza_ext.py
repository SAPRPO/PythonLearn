#save information about a pizza being ordered
pizza = {
    'crust': ['thick', 'fat'],
    'toppings': ['mushrooms', 'extra cheese']
}
#summarize the order
var = pizza['crust'][0]
print(var)
print(f"You ordered a {var}-crust pizza  " #разбиение строки
      "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")
