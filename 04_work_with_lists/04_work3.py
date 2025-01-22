#copy list

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] # если не добавить [:], оба списка будут дополняться одновременно, т.к. переменная friend_foods связана со списком, хранящимся в переменной my_foods

print(my_foods)
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')

print(my_foods)
print(friend_foods)

for mf in my_foods:
    print(mf)
print('\n----------------------\n')
for friend_food in friend_foods:
    print(friend_food)
