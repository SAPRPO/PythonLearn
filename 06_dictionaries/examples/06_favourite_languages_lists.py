favourite_languages = {
'jen' : ['python', 'ruby'],
'sarah' : ['с'],
'edward' : ['rust', 'go'],
'phil' : ['python', 'haskell'],
}

for name, languages in favourite_languages.items():
    if len(languages) != 1:
        print(f'\n{name.title()} likes the following languages:')
        for language in languages:
            print(f'\t{language.title()}')
    else:
        print(f'\n{name.title()} likes the following language:')
        for language in languages:
            print(f'\t{language.title()}')
