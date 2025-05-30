from pathlib import Path
import json

relative_filepath= '10_files_exceptions/examples/save_data/'
numbers = [2,3,5,7,11,13]

path = Path(f"{relative_filepath}numbers.json")
contents = json.dumps(numbers) #generate json-string
#contents = path.write_text(str(numbers))

path.write_text(contents)