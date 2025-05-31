from pathlib import Path
import json

relative_filepath= '10_files_exceptions/examples/save_data/'

def get_stored_user_name(path):
    if path.exists():
        contents = path.read_text()
        user_name = json.loads(contents)
        return user_name
    else:
        return None

def get_new_user_name(path):
    user_name = input(f"What is your name? ")
    contents = json.dumps(user_name)
    path.write_text(contents)
    return user_name

def greet_user():
    path = Path(f'{relative_filepath}username.json')
    user_name = get_stored_user_name(path)
    if user_name:
        print(f"Welcome back, {user_name}!")
    else:
        user_name = get_new_user_name(path)
        print(f"We will remember, if you come back {user_name}!")

greet_user()