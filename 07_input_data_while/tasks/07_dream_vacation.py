response={}

ask_name = 'What is your name? '
ask_place = 'If you could visit one place in the world, where would you go? '

polling_active = True

while polling_active:
    name = input(ask_name.title())
    place = input(ask_place)
    response[name]=place #!!![key]=value
    continue_polling = input('Would you like to let another person respond? (yes/no) ')
    if continue_polling == 'no':
        polling_active = False

print('\n ---Poll Results---')
for name,place in response.items():
    print(f'{name} would like to visit {place}')    