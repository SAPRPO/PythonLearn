import matplotlib.pyplot as plt
#sudo apt install python3-matplotlib
#in Windows?
input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
#использование стилей
plt.style.use('Solarize_Light2')
fig, ax  = plt.subplots()
#ax.plot(squares)
ax.plot(input_values, squares, linewidth = 3)
#заголовок и метки осей
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=24)
ax.set_ylabel("Square of Value", fontsize=14)

#задание размера шрифта и делений на осях
ax.tick_params(labelsize=14)
print(plt.style.available)
plt.show()