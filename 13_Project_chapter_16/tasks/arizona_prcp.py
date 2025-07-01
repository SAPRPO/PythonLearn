from pathlib import Path
from datetime import datetime

import matplotlib.pyplot as plt
import csv

from whoami import Whoami
filename = '4059352.csv'
p_temp = Whoami.get_path(filename)

path = Path(p_temp)

#Whoami.check_path(path)

lines = path.read_text().splitlines()
reader = csv.reader(lines)

header_row = next(reader)

#print header row 
for index, column_header in enumerate(header_row):
    print(index, column_header)

dates, highs = [], []

for row in reader:
    current_date = datetime.strptime(row[2],"%Y-%m-%d")
    try:
        high = float(row[5])

    except:
        print(f'value in {header_row[5]} is missing')
    else:
        highs.append(high)
        dates.append(current_date)

print(highs)

plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(dates, highs, color = 'red')
ax.set_title('prcp in Phoenix 2015')

fig.autofmt_xdate() #format datetime
ax.tick_params(labelsize=10)

plt.show()