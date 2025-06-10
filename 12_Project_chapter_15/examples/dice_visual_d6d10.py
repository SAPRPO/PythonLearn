from die import Die
import plotly.express as px

die1 = Die()
die2 = Die(10)

results = []

for roll_num in range(50_000):
    result = die1.roll() + die2.roll()
    results.append(result)

#print(results)
#анализ результатов
frequencies = []
max_result = die1.num_sides + die2.num_sides
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
#test
#print(frequencies)
#Визуализация результатов
title = "Results of Rolling One D6 and D10 50 000 times"
labels ={'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y = frequencies, title=title, labels=labels)
#далее
fig.update_layout(xaxis_dtick=1)
#показ графика
#fig.show()
#Сохранение в файл
fig.write_html('dice_visual_d6d10.html')