#Заполнение словаря данными, введенным пользователем
responses = {}
#flag
polling_active = True
while polling_active:
    name = input("\nWhat is your name?") 
    response = input("Which mountain would you like to climb someday?") #answer
    responses[name] = response #value

    repeat = input("Would you like to let another person respond? (yes/no)")
    if repeat == 'no':
        polling_active = False
#after 
print("\n---Poll Results---")
for name,response in responses.items():
    print(f"{name} would like to climb {response}.")    