from pathlib import Path
import json

relative_filepath= '10_files_exceptions/examples/save_data/'

path = Path(f'{relative_filepath}username.json')
if path.exists():
    contents = path.read_text()
    user_name = json.loads(contents)
    print(f"Welcome back, {user_name}!")
else:
    user_name = input(f"What is your name? ")
    contents = json.dumps(user_name)
    path.write_text(contents)
    print(f"We will remember, if you come back {user_name}!")