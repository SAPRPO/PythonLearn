import matplotlib.pyplot as plt

#X
input_values_x = range(-2500, 2500)
#Y
input_values_y = [x**3 for x in input_values_x ]

plt.style.use('ggplot')
fig, ax = plt.subplots()

ax.plot(input_values_x,input_values_y, linewidth =3) # линия
#ax.scatter(input_values_x,input_values_y, s =10) #точки

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=24)
ax.set_ylabel("Square of Value", fontsize=14)
ax.ticklabel_format(style="plain")
ax.axis([-300,300,-1_100_000,1_100_000])

plt.show()