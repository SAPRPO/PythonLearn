from pathlib import Path
relative_filepath = '10_files_exceptions/tasks/exceptions/'

print("----------10.7---------")

path = Path(f"{relative_filepath}numbers.txt")
count = 0
numbers = ''
while count < 4:
    try:
        number = int(input(f"Enter {count+1} number: "))
        count = count+1
    except ValueError:    
        pass
    else:
        numbers += str(number) + '\n'

print(f"Contents of numbers.txt:\n{numbers}")
path.write_text(numbers)