from pathlib import Path
import csv

import matplotlib.pyplot as plt

#relative filepath
relative_filepath = '/home/xxx/Work/PythonLearn/13_Project_chapter_16/'
#Object path
path = Path(f"{relative_filepath}/weather_data/sitka_weather_07-2021_simple.csv")
#take strings
lines = path.read_text().splitlines()
x= len(lines)
#parsing strings
reader = csv.reader(lines)

header_row = next(reader) #next -next string (our rows headers) Must be read!
print(header_row)

#print headers, positions

for index, colomn_header in enumerate(header_row): #enumerate return index
    print(index, colomn_header)

#eject and reading data

highs =[]
for row in reader:
    high = int(row[4])
    highs.append(high)
    
print(highs)

#make diagram    
#diagram data
plt.style.use('seaborn') #style
fig, ax = plt.subplots()
ax.plot(highs, color='red')

#Format diagram
ax.set_title('Daily High Temperatures, July 2021, fontsize=24')
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize =16)
ax.tick_params(labelsize=16)

plt.show()