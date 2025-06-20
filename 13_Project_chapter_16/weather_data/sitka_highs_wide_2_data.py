from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

#relative filepath
#relative_filepath = '/home/xxx/Work/PythonLearn/13_Project_chapter_16/' #Ubuntu virtual
relative_filepath = '/home/ilia/Work/PythonLearn/13_Project_chapter_16/'
#Object path
path = Path(f"{relative_filepath}/weather_data/sitka_weather_2021_simple.csv")
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

dates, highs, lows =[], [], []
for row in reader:
    #add datetime
    current_date= datetime.strptime(row[2], '%Y-%m-%d')
    #
    high = int(row[4])
    low = int(row[5])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)
    
#print(highs)

#make diagram    
#diagram data
plt.style.use('seaborn') #style
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')
ax.plot(dates, lows, color='blue')
#Format diagram
ax.set_title('Daily High Temperatures, July 2021', fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize =16)
fig.autofmt_xdate() #format datetime
ax.tick_params(labelsize=16)

plt.show()