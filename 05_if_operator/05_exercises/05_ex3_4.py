#age = 14

age = int(input("Введите возраст: "))
if age < 2:
    print("младенец")
elif age < 4:
    print("малыш")
elif age < 13:
    print("ребенок")
elif age < 20:
    print("подросток")
elif age < 65:
    print("взрослый")
else:
    print("пожилой")
