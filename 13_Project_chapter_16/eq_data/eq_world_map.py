from pathlib import Path
import json

import plotly.express as px
import pandas as pd
from whoami import Whoami

filename = 'eq_data_1_day_m1.geojson'

#Read text
path = Path(Whoami.get_path(filename))
#Whoami.check_path(path)
contents = path.read_text()
all_eq_data = json.loads(contents)

#Convert to easy reading
#path1 = Path(f'{Whoami.get_path_dirname(path)}/readable_eq_data.geojson')
#readable_contents = json.dumps(all_eq_data, indent=4)
#path1.write_text(readable_contents)

#all earthquakes

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

#magnitude, latitude, longitude
mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][0]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:10])
print(lats[:10])
#diagramm

#df = pd.DataFrame()
title = 'Global Earthquakes'
fig = px.scatter_geo( lat=lats, lon=lons, size=mags  ,title=title)
fig.show()

