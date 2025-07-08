from pathlib import Path
import csv, sys
from datetime import datetime
import matplotlib.pyplot as plt
#from sympy.physics.units import current
import plotly.express as px
from whoami import Whoami

filename = 'world_fires_1_day.csv'
path = Path(Whoami.get_path(filename))

def get_reader(_path):
    lines = _path.read_text().splitlines()
    _reader = csv.reader(lines)
    return _reader

def print_highs(highs):
    count = 1
    for d in highs[:10]:
        print(f"{count} {d}")
        count = count+1

reader = get_reader(path)
h_row = next(reader)

def index_return(header, hrow):
    for index, c_header in enumerate (hrow):
        if header == c_header:
            print(f'index {header} = {index}, in')
            return index
    print(f"No header {header}!\nCheck values\nProgram interrupted!!!")
    return sys.exit()

index_latitude = index_return('latitude', h_row)
index_longitude = index_return('longitude', h_row)
index_brightness = index_return('brightness', h_row)
index_data = index_return('acq_date', h_row)
lats, lons, brightness, acq_date = [],[],[],[]
for data in reader:
    #current_date = datetime.strptime(data[index_data], "%Y-%m-%d")
    try:
        lat = float(data[index_latitude])
        lon = float(data[index_longitude])
        bright = float(data[index_brightness])
        acq = data[index_data]
    except:
        print(f"Value in  is missing")
    else:
        lats.append(lat)
        lons.append(lon)
        brightness.append(bright)
        acq_date.append(acq)


print(h_row)
print(lats[:10])
print(lons[:10])
print(brightness[:10])
print(acq_date[:10])

#diagram

title = 'Global Fires'

fig = px.scatter_geo(lat=lats, lon=lons, size=brightness, title=title,
                     color = brightness,
                     color_continuous_scale='agsunset',
                     labels={'color':'Fire'},
                     projection='natural earth', #orthographic
                     hover_name=acq_date,
                     )

fig.show()