from pathlib import Path
import json

relative_filepath= '10_files_exceptions/examples/save_data/'
path = Path(f"{relative_filepath}numbers.json")
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)