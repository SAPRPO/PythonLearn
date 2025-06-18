#three D6 cube
from die import Die
import plotly.express as px

die1 = Die()
die2 = Die()
#die3 = Die()

results =[]

for roll_num in range(1000):
    result = die1.roll() * die2.roll() #+ die3.roll()
    results.append(result)

frequencies = []
max_result = die1.num_sides + die2.num_sides #+die3.num_sides
poss_results = range(2,max_result+1)

for value in poss_results:
    freq = results.count(value)
    print(freq)
    frequencies.append(freq)


#Визуализация
title = "Results of Rolling two D6 1000 times"
labels ={'x': 'Result', 'y': 'Frequency of Result'}
 
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.show()