from pathlib import Path
#need to open from ex 10
full_path = 'C:/Users/User/source/repos/PythonLearn/10_files_exceptions/examples/readfromfile/' # use / instead \\
relative_filepath = '10_files_exceptions/examples/readfromfile/'
path = Path(f'{full_path}/pi_digits.txt') #or relative filepath
#contents = path.read_text()
#remove empty string
#contents = contents.rstrip()
#or
contents = path.read_text().rstrip() #method chaining
print(contents)
