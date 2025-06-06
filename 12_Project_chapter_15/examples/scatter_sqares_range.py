import matplotlib.pyplot as plt
#построение по точкам
#добавление точек
x_values = range(-1001, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.scatter(x_values,y_values, c='green',s= 10) #можно и в rgb (0,0.8,0)
#ax.scatter(x_values,y_values, c=y_values, cmap=plt.cm.Blues,s= 10) #градиент

plt.show()

#задание заголовка диаграммы и меток осей:
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=24)
ax.set_ylabel("Square of Value", fontsize=14)

#задание диапазона для каждой оси
ax.axis([0,1100,0,1_100_000])
#не используя научную запись
ax.ticklabel_format(style='plain')
plt.show()
#автосохранение диаграмм
plt.savefig('squares_plot.png', bbox_inches='tight')

#задание размера шрифта и делений на осях
ax.tick_params(labelsize=14)