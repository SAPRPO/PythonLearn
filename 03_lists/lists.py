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
# 
guests=['Сергей', 'Александр', 'Алена', 'Андрей']
print(guests)
invitation="Приглашаю на праздник!"

invitation_mes0= f"{guests[0]}, {invitation}"
invitation_mes1= f"{guests[1]}, {invitation}"
invitation_mes2= f"{guests[2]}, {invitation}"
invitation_mes3= f"{guests[3]}, {invitation}"

print(invitation_mes0)
print(invitation_mes1)
print(invitation_mes2)
print(invitation_mes3)

lost=guests[1]
guests.remove(lost)
print(lost)
print(guests)
guests.insert(0, 'Леха')
print(guests)
print("New Invitarion list")
print(invitation_mes0)
print(invitation_mes1)
print(invitation_mes2)
print(invitation_mes3)

print("I founded large table!")

guests.append('Екатерина')
guests.insert(0, 'Ксения')
guests.insert(3, 'Николай')
print(guests)

#short list
print("ShortList")
print(f"Sorry {guests.pop()} I can't invite you!")
print(f"Sorry {guests.pop()} I can't invite you!")
print(f"Sorry {guests.pop()} I can't invite you!")
print(f"Sorry {guests.pop()} I can't invite you!")
print(f"Sorry {guests.pop()} I can't invite you!")
print(guests)
del guests[1]
del guests[0]

print(guests)