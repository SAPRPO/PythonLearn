import matplotlib.pyplot as plt
#построение по точкам
#добавление точек
x_values = [1,2,3,4,5]
y_values = [1,4,9,16,25]

plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.scatter(x_values,y_values, s= 100)
plt.show()

#задание заголовка диаграммы и меток осей:
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=24)
ax.set_ylabel("Square of Value", fontsize=14)

#задание размера шрифта и делений на осях
ax.tick_params(labelsize=14)