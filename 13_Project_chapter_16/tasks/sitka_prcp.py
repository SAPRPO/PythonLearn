from pathlib import Path
from datetime import datetime

import matplotlib.pyplot as plt
import csv
#username in system
from whoami import Whoami

user = Whoami.get_user_name()
relative_filepath = f'/home/{user}/Work/PythonLearn/13_Project_chapter_16/'

path = Path(f"{relative_filepath}/tasks/sitka_weather_2021_full.csv")
print(path)
Whoami.check_path(path)

    
#разбор файла

lines = path.read_text().splitlines() #разбиение на строки
#csv
reader = csv.reader(lines)
#header
header_row = next(reader)
#print headers
for index, column_header in enumerate(header_row):
    print(index, column_header) 
#формирование списков для построения диаграммы

dates, highs = [],[]
missing = []
for row in reader:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    try:
        high = float(row[5])
    except:
        print(f"Value in {header_row[5]} is missing")
        mes = f"value in {row} is missing"
        missing.append(mes)
    else:
        dates.append(current_date)
        highs.append(high)

#print(highs[:10])
#max1 = max(highs)
#min1 = min(highs)
#print(min1, max1) 

for m in missing:
    print(m)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, color ='green')

ax.set_title('PRCP 2021', fontsize=20)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("PRCP", fontsize =16)
fig.autofmt_xdate() #format datetime
ax.tick_params(labelsize=10)

plt.show()