import sys
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

#for index, column_header in enumerate(hrow_dv):
#    print(index, column_header)

def index_return(header, hrow):
    for index, c_header in enumerate (hrow):
        if header == c_header:
            print(f'index {header} = {index}, in')
            return index
    print(f"No header {header}!\nCheck values\nProgram interrupted!!!")
    return sys.exit()

#def get_station_name(c_name, hrow):
#    for c_name in hrow[:2]:
 #       print(c_name)

#v = get_station_name('NAME', hrow_sitka)

index_date = index_return('DATE', hrow_sitka) #everything coloumn
index_tmax_sitka = index_return('TMAX', hrow_sitka)
index_tmax_dv = index_return('TMAX', hrow_dv)


dates, highs_sitka, highs_dv = [],[],[]
#missing =[]


for row in reader_sitka:
    current_date = datetime.strptime(row[index_date], "%Y-%m-%d")
    try:
        high = float(row[index_tmax_sitka])
    except:
        print(f"Value in {hrow_sitka[index_tmax_sitka]} is missing")
    else:
        highs_sitka.append(high)

        dates.append(current_date)



#print(highs_sitka) 

#test print #use methods for circle for

for row in reader_dv:
    #current_date = datetime.strptime(row[2], "%Y-%m-%d")
    try:
        high = float(row[index_tmax_dv])
    except:
        print(f"Value in {hrow_dv[index_tmax_dv]} is missing")
    else:
        highs_dv.append(high)
        #dates.append(current_date)

print_highs(highs_sitka)
print('\n')
print_highs(highs_dv)

#var1 = len(highs_dv)
#var2 = len(highs_sitka)




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