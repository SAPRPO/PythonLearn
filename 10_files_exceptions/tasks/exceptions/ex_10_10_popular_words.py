#find popular words in text!
from pathlib import Path

relative_filepath = '10_files_exceptions/tasks/exceptions/'
path = Path(f"{relative_filepath}S.txt")

try:
    contents = path.read_text(encoding='utf-8')
except Exception:
    print(f"Error open!")
else:
    print(f"{path.name} successfully read")

keyword = 'командир'

lines = contents.splitlines()
repeat = 0
string_index=1
for line in lines:
    count_word= line.lower().count(keyword)
    repeat += count_word
    string_index =string_index+1


print(f"Keyword '{keyword}' repeated {repeat} times")
