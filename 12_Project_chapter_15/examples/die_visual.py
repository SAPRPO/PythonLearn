from die import Die
import plotly.express as px
#test
die = Die()

results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

#print(results)
#анализ результатов
frequencies = []
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

#print(frequencies)
#Визуализация результатов
title = "Results of Rolling One D6 1000 times"
labels ={'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y = frequencies, title=title, labels=labels)
fig.show()