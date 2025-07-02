from pathlib import Path
from datetime import datetime

import matplotlib.pyplot as plt

from whoami import Whoami
import csv

filename_1 = 'sitka_weather_2021_full.csv'
filename_2 = 'death_valley_2021_full.csv'
filename_3 = '4059371.csv'


path_sitka = Path(Whoami.get_path(filename_1))
path_dv = Path(Whoami.get_path(filename_2))
path_sf = Path(Whoami.get_path(filename_3))

def get_reader(path):
    lines = path.read_text().splitlines()
    print(f'{len(lines)}')
    reader = csv.reader(lines)
    return reader

def test_print(highs):
    count = 1
    for d in highs[:10]:
        print(f"{count} {d}")
        count = count+1

reader_sitka = get_reader(path_sitka)
reader_dv= get_reader(path_dv)
reader_sf = get_reader(path_sf)

row_sitka = next(reader_sitka)
row_dv = next(reader_dv)
row_sf = next(reader_sf)

dates, highs_sitka, highs_dv, highs_sf = [],[],[],[]

for row in reader_sitka:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    try:
        print(row[5])
        high = float(row[5])
    except:
        print(f"Value in {row_sitka[5]} is missing")
    else:
        highs_sitka.append(high)
        dates.append(current_date)

for row in reader_dv:
    try:
        print(row[3])
        high = float(row[3])
    except:
        print(f"Value in {row_dv[3]} is missing")
    else:
        highs_dv.append(high)

for row in reader_sf:
    try:
        high = float(row[3])
    except:
        print(f"Value in {row_sf[3]} is missing")
    else:
        highs_sf.append(high)

#test_print(highs_sitka)
#print('\n')
#test_print(highs_dv)
#print('\n')
#test_print(highs_sf)
#print('\n')

#for index, column_header in enumerate(row_sitka):
#    print(index, column_header)

#diagram

plt.style.use('classic') #sea
fig, ax = plt.subplots()
ax.plot(dates[:100], highs_sitka[:100], color ='blue')
ax.plot(dates[:100], highs_dv[:100], color ='red')
ax.plot(dates[:100], highs_sf[:100], color ='green')

ax.set_title('Max PRCP in Sitka (blue)\nDeath Valley (red) 2021', fontsize=20)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Max temperature F", fontsize =16)

fig.autofmt_xdate() #format datetime
ax.tick_params(labelsize=10)

plt.show()