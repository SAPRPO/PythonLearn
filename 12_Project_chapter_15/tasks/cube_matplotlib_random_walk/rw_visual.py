import plotly.express as px

from random_walk import RandomWalk

rw = RandomWalk() #5000 as default
while True:
    rw.fill_walk()

    #нанесение точек на диаграмму
    #plt.style.use(style='classic')
    #Изменение размера заполнения экрана
    #fig, ax = plt.subplots(figsize=(16,9)) #fig - весь рисунок, ax, одна из диаграмм
    #форматирование 
    #point_numbers= range(rw.num_points) #генерирование списка чисел
    #ax.plot(rw.x_values, rw.y_values, linewidth =1) #test add
    #ax.set_aspect('equal') #обе оси имеют равное расстояние между делениями
    #выделение первой и последней точки
    #ax.scatter(0,0,c='green', edgecolor='none', s=100) # 1-я точка
    #ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s =100) #последняя точка
    #Удаление осей
    #ax.get_xaxis().set_visible(False)
    #ax.get_yaxis().set_visible(False)
    #plt.show()
    title = "Results"
    labels ={'x': 'Result', 'y': 'Frequency of Result'}
    fig =px.bar(x=rw.x_values, y=rw.y_values,title=title, labels=labels)
    fig.update_layout(xaxis_dtick=1)
    fig.show()
    
    keep_running=input("Make another walk? (y/n): ") #add try/except for y/n
    if keep_running == 'n':
        break