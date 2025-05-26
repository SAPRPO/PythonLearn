from pathlib import Path

relative_filepath= '10_files_exceptions/examples/readfromfile/'
path = Path(f'{relative_filepath}/pi_digits.txt')
contents = path.read_text()

#lines
lines = contents.splitlines()
for line in lines:
    print(line)