#send any arguments
def make_pizza(*toppings):
    #print(toppings)
    #('pepperoni',)
    #('pepperoni', 'green peppers', 'extra cheese')
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
# *toppings means we don't know how many toppings will be passed to the function

make_pizza('pepperoni',)
make_pizza('pepperoni', 'green peppers', 'extra cheese')

#positional argument before *toppings

def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
#size is a positional argument

size = int(input("What size pizza do you want? "))
make_pizza(size, 'pepperoni',)
make_pizza(12, 'pepperoni', 'green peppers', 'extra cheese')

