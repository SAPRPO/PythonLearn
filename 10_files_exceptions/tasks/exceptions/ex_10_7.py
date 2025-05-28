from pathlib import Path
relative_filepath = '10_files_exceptions/tasks/exceptions/'

print("----------10.7---------")

path = Path(f"{relative_filepath}numbers.txt")
count = 0
numbers = ''
while count < 4:
    try:
        number = int(input("Enter number: "))
        count = count+1
    except ValueError:    
        print("Not a number! Try again!")
    else:
        numbers += str(number) + '\n'
path.write_text(numbers)