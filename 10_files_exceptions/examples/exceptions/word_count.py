from pathlib import Path
"""Подсчитывает количество строк в файле."""
def count_words(path):
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"File {path} doesn't exist")
    else:
        words = contents.split() #get words from text with ,
        #for w in words:
        #    print(f"{w}") 
        num_words = len(words)
        print(f"The file {path.name} has about {num_words} words.")


relative_filepath = '10_files_exceptions/examples/exceptions/'
path = Path(f"{relative_filepath}alice.txt")
count_words(path)

filenames = ['alice.txt','xxx.txt','aaa.txt']
for filename in filenames:
    path = Path(f"{relative_filepath}{filename}")
    count_words(path)

