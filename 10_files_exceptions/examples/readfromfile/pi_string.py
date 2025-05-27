from pathlib import Path

relative_filepath= '10_files_exceptions/examples/readfromfile/'
path = Path(f'{relative_filepath}/pi_digits.txt')

contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()  #strip() - removing spaces

print(pi_string)
print(len(pi_string)) 

