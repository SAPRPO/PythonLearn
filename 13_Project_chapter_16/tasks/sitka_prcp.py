from pathlib import Path
from datetime import datetime

import matplotlib.pyplot as plt
import csv

#relative_filepath = '/home/xxx/Work/PythonLearn/13_Project_chapter_16/' #Ubuntu virtual

#relative_filepath = '/home/ilia/Work/PythonLearn/13_Project_chapter_16/'

relative_filepath = '/home/user_deb/Work/PythonLearn/13_Project_chapter_16/'

path = Path(f"{relative_filepath}/tasks/sitka_weather_2021_full.csv")

print(path)
if path.exists():
    print("ok")
else:
    print("error")

#разбор файла
lines = path.read_text().splitlines() #рызбиение на строки

#csv
reader = csv.reader(lines)
#header
header_row = next(reader)
#print headers
for index, column_header in enumerate(header_row):
    print(index, column_header) 

#формирование списков для построения диаграммы