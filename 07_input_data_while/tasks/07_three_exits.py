toppings = []
active = True
while active:
    topping = input("Enter a topping (or 'quit' to finish): ")
    if topping.isdigit():
        break
    
    if topping.lower() == 'quit':
        break
    else:
        toppings.append(topping)
        print(f"You've added {topping} to your pizza.")
    if len(toppings) >= 3:
        print("You've added more than three toppings. Your pizza will be extra special!")
        active = False

print("Your pizza toppings are:")
count = 1
for topping in toppings:    
    print(f"{count}. {topping}")
    count += 1
