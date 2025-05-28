from pathlib import Path
relative_filepath = '10_files_exceptions/examples/exceptions/'

path = Path(f"{relative_filepath}alice_.txt")
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"File {path} doesn't exist")