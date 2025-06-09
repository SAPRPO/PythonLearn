import matplotlib.pyplot as plt

from random_walk import RandomWalk

rw = RandomWalk() #5000 as default
rw.fill_walk()

#нанесение точек на диаграмму
plt.style.use(style='classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
ax.set_aspect('equal') #обе оси имеют равное расстояние между делениями
plt.show()
#360