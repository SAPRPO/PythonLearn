requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print('Hold the anchovies!')

requested_topping = ['mushrooms', 'anchovies', 'spinach', 'pineapple']
if 'mushrooms' in requested_topping:
    print(requested_topping[0] == 'mushrooms' ) 
else:
    print('False')       