from pathlib import Path
import json

relative_filepath= '10_files_exceptions/examples/save_data/'

path = Path(f'{relative_filepath}username.json')
contents = path.read_text()
user_name = json.loads(contents)
print(f'Welcome back, {user_name}!')