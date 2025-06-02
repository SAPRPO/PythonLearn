from pathlib import Path
import json

relative_filepath= '10_files_exceptions/tasks/save_data/ex10_12/'

def read_number(path):
    if path.exists():
        contents = path.read_text() #reading
        number = json.loads(contents) #convert

        return number
    else: 
        return None

def write_number(path):
    number = int(input("Enter your favourite number: ")) #enter number
    contents = json.dumps(number) #convert to json
    path.write_text(contents) #write to text


def favourite_number():
    path = Path(f"{relative_filepath}number.json") # save path to write
    number = read_number(path)
    if number:
        print(f'Your favourite number is: {number}')
    else:
        write_number(path)
        print(f'Your favourite number: {number} written in {path}')

favourite_number()