from pathlib import Path
import csv

#relative_filepath = '/home/xxx/Work/PythonLearn/13_Project_chapter_16/' #Ubuntu virtual
relative_filepath = '/home/ilia/Work/PythonLearn/13_Project_chapter_16/'

path = Path(f"{relative_filepath}/weather_data/death_valley_2021_simple.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, coloumn_header in enumerate(header_row):
    print(index, coloumn_header) 

    #387