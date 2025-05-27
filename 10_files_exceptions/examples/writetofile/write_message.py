from pathlib import Path

relative_filepath = '10_files_exceptions/examples/writetofile/'
#path = Path(f'{relative_filepath}/pi_digits.txt') #or relative filepath
#print('write one string to file:')
path = Path(f'{relative_filepath}programming.txt')
path.write_text("I love programming!")

#print('write three string to file:') #override previous contents

contents = "I love programming! \n"
contents += "I love creating new games! \n"
contents += "I also love to work with data! \n"

path.write_text(contents)