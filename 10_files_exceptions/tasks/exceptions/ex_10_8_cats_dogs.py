from pathlib import Path

relative_filepath = '10_files_exceptions/tasks/exceptions/'
def fileRead(path):  # check in function
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"File {path.name} doesn't exist")
    else:
        print(f"File {path.name} exist")
        printContents(contents)

def printContents(contents):
     print(f"{contents}\n")

animals = ['cats.txt', 'dogs.txt', 'birds.txt']

for animal in animals:
        animal = Path(f"{relative_filepath}{animal}") #create Path to file
        fileRead(animal) #try to read 
