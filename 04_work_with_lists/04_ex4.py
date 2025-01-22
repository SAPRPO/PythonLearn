players = ['charles', 'martina', 'ivan', 'mike', 'alex']

print(f"Первые три пункта в списке эти:\n{players[:3]}")
print(f"Первые три пункта из середины списка:\n{players[1:4]}")
print(f"последние три пункта в списке эти:\n{players[-3:]}")

my_pizzas= ['carbonara', 'barbeque', 'cheese']
friends_pizzas = my_pizzas[:]
my_pizzas.append('salami')
friends_pizzas.append('pepperoni')

print("Мои любимые пиццы:")
for mp in my_pizzas:
    print(mp)
print('\n----------------------\n')
print("Любимые пиццы моего друга:")
for fp in friends_pizzas:
    print(fp)