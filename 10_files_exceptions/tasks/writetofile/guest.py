from pathlib import Path

relative_filepath = '10_files_exceptions/tasks/writetofile/'
print("----------10.4---------")
guest = input("What is your name: ")
path = Path(f"{relative_filepath}guest.txt")
path.write_text(guest)

print("----------10.5---------")
path = Path(f"{relative_filepath}guest_book.txt")
count = 0
name = ''
while count < 4:
    name += input("Hello! What is your name?\n") + '\n'
    count = count+1
path.write_text(name)


