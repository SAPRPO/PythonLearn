from die import Die
import matplotlib.pyplot as plt
from random_walk import RandomWalk

die1 = Die()
die2 = Die()

result = die1.roll() + die2.roll()
results = [die1.roll() + die2.roll() for result in range(100)]

frequencies=[]
max_result = die1.num_sides +die2.num_sides
poss_results = range(2,max_result+1)

frequencies = [results.count(freq) for freq in poss_results]
print(f"frequencies length: {len(frequencies)}, results length: {len(results)}")
#visualise with matplotlib
#lines #add conditions lines or scatter
question = input("For lines/scatter graph press y/n:\n")
if question == 'y':
    plt.style.use('ggplot') 
    fig, ax = plt.subplots()

    ax.plot(frequencies, results[:11],linewidth = 3) #11 combinations

    ax.set_title("Square Numbers", fontsize=24)
    ax.set_xlabel("Value", fontsize=24)
    ax.set_ylabel("Square of Value", fontsize=14)
    ax.ticklabel_format(style="plain")
    ax.axis([-30,30,0,30])

    plt.show()
else:
#scatter
    #rw = RandomWalk(100)
    plt.style.use(style='classic')

    fig, ax = plt.subplots(figsize=(16,9)) 
    ax.scatter(frequencies, results[:11])
    #point_numbers= range(rw.num_points)
    #ax.plot(rw.x_values, rw.y_values, linewidth =1)
    #ax.set_aspect('equal')
    plt.show()

    