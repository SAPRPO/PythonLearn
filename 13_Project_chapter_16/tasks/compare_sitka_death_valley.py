from pathlib import Path
from datetime import datetime

import matplotlib.pyplot as plt
#import seaborn as sns
from whoami import Whoami 
import csv

filename_1 = 'sitka_weather_2021_full.csv'
filename_2 = 'death_valley_2021_full.csv'
p_temp1 = Whoami.get_path(filename_1)
p_temp2 = Whoami.get_path(filename_2)

path_sitka = Path(p_temp1)
path_dv = Path(p_temp2)

def get_reader(path):
    lines = path.read_text().splitlines()
    reader = csv.reader(lines)
    return reader

def print_highs(highs):
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

print_highs(highs_sitka)
print('\n')
print_highs(highs_dv)

#var1 = len(highs_dv)
#var2 = len(highs_sitka)


#for index, column_header in enumerate(hrow_dv):
#    print(index, column_header) 

#diagram 
#sns.set_theme()
plt.style.use('classic') #sea
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