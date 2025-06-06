import matplotlib.pyplot as plt
#построение по точкам
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(2,4, s= 200)
plt.show()

#задание заголовка диаграммы и меток осей:
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=24)
ax.set_ylabel("Square of Value", fontsize=14)

#задание размера шрифта и делений на осях
ax.tick_params(labelsize=14)