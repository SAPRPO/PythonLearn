from pathlib import Path

relative_filepath = '10_files_exceptions/tasks/readfromfile'
path = Path(f"{relative_filepath}/learning_python.txt")

print("--------10.1-----------")
contents = path.read_text(encoding='utf-8')
print(contents)
print("--------10.1 part 2-----------")

lines = contents.splitlines()
py_string =''
for line in lines:
    py_string += line+ '\n'

print(py_string)

print("--------10.2 replace-----------")
print("--------10.2 by lines-----------")
cpp_string=''
for line in lines:
    cpp_string += line.replace('Python', 'C++') + '\n'

print(cpp_string)

print("--------10.2 in contents-----------")
contents =contents.replace('Python', 'C++')
print(contents)


print("--------10.3 remove spaces between strings-----------")
cpp2=''
for line in contents.splitlines():
    cpp2+=line

print(cpp2)