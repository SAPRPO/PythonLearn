from pathlib import Path

relative_filepath= '10_files_exceptions/examples/readfromfile/'
path = Path(f'{relative_filepath}/pi_million_digits.txt')

contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()  #strip() - removing spaces

birthday = input("Enter your birthday, in form mmddyy: ")
if birthday in pi_string:
    print(f"Yes. Your birthday {birthday} in PI")
else:
    print(f"No. You birthday {birthday} not in PI")