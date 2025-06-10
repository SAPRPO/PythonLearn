import matplotlib.pyplot as plt

from random_walk import RandomWalk

rw = RandomWalk() #5000 as default
while True:
    rw.fill_walk()

    #нанесение точек на диаграмму
    plt.style.use(style='classic')
    #Изменение размера заполнения экрана
    fig, ax = plt.subplots(figsize=(16,9)) #fig - весь рисунок, ax, одна из диаграмм
    #форматирование 
    point_numbers= range(rw.num_points) #генерирование списка чисел
    ax.scatter(rw.x_values, rw.y_values,c = point_numbers,  cmap = plt.cm.Blues, edgecolor='none', s=15) #test add
    ax.set_aspect('equal') #обе оси имеют равное расстояние между делениями
    #выделение первой и последней точки
    ax.scatter(0,0,c='green', edgecolor='none', s=100) # 1-я точка
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s =100) #последняя точка
    #Удаление осей
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    keep_running=input("Make another walk? (y/n): ") #add try/except for y/n
    if keep_running == 'n':
        break