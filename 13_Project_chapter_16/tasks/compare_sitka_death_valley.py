from pathlib import Path
from datetime import datetime

import matplotlib.pyplot as plt

from whoami import Whoami 
import csv

p = Whoami.get_path()
relative_filepath = f'{p}/13_Project_chapter_16/'

path_sitka = Path(f"{relative_filepath}/tasks/sitka_weather_2021_full.csv")
path_dv = Path(f"{relative_filepath}/tasks/death_valley_2021_full.csv")

Whoami.check_path(path_sitka)
Whoami.check_path(path_dv)

def get_reader(path):
    lines = path.read_text().splitlines()
    reader = csv.reader(lines)
    return reader

def test_print(highs):
    count = 1
    for d in highs[:10]:
        print(f"{count} {d}")
        count = count+1

#def get_lists_y(header_row, reader, row):
#    highs=[]  
#    for r in reader:
#        try:
#            high = float(r[row])
#        except:
#            print(f"Value in {header_row[row]} is missing")
#        else:
#            highs.append(high)
#            return highs
        

reader_sitka = get_reader(path_sitka)
reader_dv= get_reader(path_dv)

hrow_sitka = next(reader_sitka)
hrow_dv = next(reader_dv)

dates, highs_sitka, highs_dv = [],[],[]
#missing =[]


for row in reader_sitka:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    try:
        high = float(row[7])
    except:
        print(f"Value in {hrow_sitka[7]} is missing")
    else:
        highs_sitka.append(high)
        dates.append(current_date)
#print(highs_sitka) 

#test print #use methods for circle for

for row in reader_dv:
    #current_date = datetime.strptime(row[2], "%Y-%m-%d")
    try:
        high = float(row[6])
    except:
        print(f"Value in {hrow_dv[6]} is missing")
    else:
        highs_dv.append(high)
        #dates.append(current_date)

test_print(highs_sitka)
print('\n')
test_print(highs_dv)

#var1 = len(highs_dv)
#var2 = len(highs_sitka)


#for index, column_header in enumerate(hrow_dv):
#    print(index, column_header) 

#diagram 
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs_sitka, color ='blue')
ax.plot(dates, highs_dv, color ='red')
ax.set_title('Max temperatures in Sitka (blue)\nDeath Valley (red) 2021', fontsize=20)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Max temperature F", fontsize =16)

fig.autofmt_xdate() #format datetime
ax.tick_params(labelsize=10)

plt.show()
#391