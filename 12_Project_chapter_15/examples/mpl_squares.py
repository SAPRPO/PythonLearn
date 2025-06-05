import matplotlib.pyplot as plt
#sudo apt install python3-matplotlib

squares = [1,4,9,16,25]
fig, ax  = plt.subplots()
ax.plot(squares)
plt.show()