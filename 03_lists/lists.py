bikes = ['trek', 'downhill', 'special']
print(bikes[0]) 
print(bikes[-1]) # вывод последнего элемента [-2] предпоследнего

message = f"My first bicycle was a {bikes[0].title()}"
print(message)

print("------Examples-------")
#3.1
names = ['Сергей', 'Александр', 'Алена', 'Андрей']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
#3.2
message=f"Мой друг {names[0]}"

print(message)
print(names)

#3.3
cars=['bmw', 'audi', 'mercedes', 'hyndai', 'chevrolet', 'lada']

mes=f"Хочу купить {cars[3].title()}"
print(mes)

cars[-1] = 'honda'
print(cars)
# добавление в конце списка
cars.append('skoda')
print(cars)
#cars = [] #пустой список
#добавление в список
cars.insert(1, 'toyota')
print(cars)
del cars[0] #удаление элементов
print(cars)

pop_cars = cars.pop()

print(pop_cars)
print(f"last car was {pop_cars.title()}") 
# удаление произвольной позиции
x=cars.pop(3)
print(x)

#удаление по значению
no_favourite='honda'
cars.remove(no_favourite)
print(cars)

#3.4
# guests

guests=[]