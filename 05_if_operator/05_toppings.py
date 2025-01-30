requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print('Hold the anchovies!')

requested_topping = ['mushrooms', 'anchovies', 'spinach', 'pineapple']
if 'mushrooms' in requested_topping:
    print(requested_topping[0] == 'mushrooms' ) 
else:
    print('False')       
print('\n----------------------------------------\n')
if 'mushrooms' in requested_topping:
    print('Adding mushrooms')
elif 'pineapple' in requested_topping:
    print('Adding pineapple')
elif 'spinach' in requested_topping:
    print('Adding spinach')

print('\nfinish making pizza')