from pathlib import Path
import json

relative_filepath= '10_files_exceptions/tasks/save_data/ex10_11/'

path = Path(f"{relative_filepath}number.json") 
contents = path.read_text() #reading
number = json.loads(contents) #convert
print(f'Your favourite number is: {number}')
