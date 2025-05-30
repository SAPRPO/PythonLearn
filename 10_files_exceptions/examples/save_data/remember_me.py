from pathlib import Path
import json

relative_filepath= '10_files_exceptions/examples/save_data/'

user_name = input("What is your name? ")

path = Path(f"{relative_filepath}username.json")
contents = json.dumps(user_name)
path.write_text(contents)

print(f"We will remeber you, {user_name}, when you come back!")
