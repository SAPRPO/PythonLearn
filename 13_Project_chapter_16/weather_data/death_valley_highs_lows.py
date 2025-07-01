from pathlib import Path
from datetime import datetime

from whoami import Whoami
import matplotlib.pyplot as plt 
import csv

filename = 'death_valley_2021_simple.csv'

path = Path(Whoami.get_path(filename))

lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, coloumn_header in enumerate(header_row):
    print(index, coloumn_header) 

dates, highs, lows = [],[],[]

for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        print(f"Missing value for {current_date}")
    else:    
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

#diagramm
plt.style.use('seaborn') #style
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')
ax.plot(dates, lows, color='blue')
#заливка
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.2)

title = "Daily High and Low Temperatures, 2021\nDaeth Valley, CA"
ax.set_title(title, fontsize=20)
ax.set_ylabel("Temperature (F)", fontsize =16)
fig.autofmt_xdate() #format datetime
ax.tick_params(labelsize=16)

plt.show()