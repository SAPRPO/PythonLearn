from pathlib import Path

relative_filepath = '10_files_exceptions/tasks/writetofile/'
print("----------10.4---------")
guest = input("What is your name: ")
path = Path(f"{relative_filepath}guest.txt")
path.write_text(guest)

