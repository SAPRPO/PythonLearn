#todo
from die import Die
import plotly.express as px

die1 = Die()
die2 = Die()
#die3 = Die()
result = die1.roll() + die2.roll()
results = [die1.roll() + die2.roll() for result in range(100)]
print(results)

#r1=[]
#for roll_num in range(10):
#    result = die1.roll() + die2.roll() #+ die3.roll()
#    r1.append(result)
#
#print("\n")
#print(r1)
frequencies=[]
max_result = die1.num_sides +die2.num_sides
poss_results = range(2,max_result+1)

#freq = [value for value in results]
frequencies = [results.count(freq) for freq in poss_results]


#for value in poss_results:
#    freq = results.count(value)
#    print(freq)
#    frequencies.append(freq)
print(frequencies)


#Визуализация
title = "Results of Rolling two D6 100 times"
labels ={'x': 'Result', 'y': 'Frequency of Result'}
 
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
#fig.show()
fig.write_html("graph")