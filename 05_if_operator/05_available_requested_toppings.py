available_toppings = ['mushrooms', 'onions', 'pineapple', 'extra cheese', 'pepperoni']

requested_toppings = ['mushrooms', 'cheese', 'pepperoni']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry, we don't have {requested_topping}")