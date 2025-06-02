from pathlib import Path
import json

relative_filepath= '10_files_exceptions/tasks/save_data/ex10_11/'

number = int(input("Enter your favourite number: ")) #enter number
path = Path(f"{relative_filepath}number.json") # save path to write
contents = json.dumps(number) #convert to json
path.write_text(contents) #write to text





