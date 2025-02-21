favourite_languages = {
'jen' : 'python',
'sarah' : 'с',
'edward' : 'rust',
'phil' : ' python',
}

language = favourite_languages['sarah'].title()
print(f"Sarah's favourite language is {language}")

for name, lang in favourite_languages.items():
    print(f"{name.title()} favourite language is {lang.title()}")

    #keys in dictionary
print("\n")

for name in favourite_languages.keys(): # for name in favourite_languages 
    print(name.title())

print("\n--------------------")

friends = ['phil', 'sarah']

for name in favourite_languages.keys():
    print(f"Hi {name.title()}")
    if name in friends:
        language = favourite_languages[name].title() # value of key
        print(f"\t{name.title()}, I see you love {language}")
        
    if 'erin' not in favourite_languages.keys():
        print("Erin, please take our poll!")