from die import Die
import plotly.express as px

die1 = Die(8)
die2 = Die(8) 

results = []
#выборка
for roll_num in range(10000): 
    res = die1.roll() + die2.roll()
    results.append(res) #диапазон 1
#print(results)
#частота
frequencies = []
max_result = die1.num_sides + die2.num_sides
poss_results = range(2, max_result+1) #Диапазон 2

for value in poss_results:
    freq = results.count(value)
    frequencies.append(freq)

#Визуализация
title = "Results of Rolling two D8 1000 times"
labels ={'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.show()