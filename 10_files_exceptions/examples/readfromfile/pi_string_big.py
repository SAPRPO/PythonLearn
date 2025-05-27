from pathlib import Path

relative_filepath= '10_files_exceptions/examples/readfromfile/'
path = Path(f'{relative_filepath}/pi_million_digits.txt')

contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()  #strip() - removing spaces

print(f"{pi_string[:52]}")
print(len(pi_string)) 

