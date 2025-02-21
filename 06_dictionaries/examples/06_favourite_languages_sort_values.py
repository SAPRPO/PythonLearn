favourite_languages = {
'jen' : 'python',
'sarah' : 'с',
'edward' : 'rust',
'phil' : 'python',
}


print("\n--------------------")

#friends = ['phil', 'sarah']

#for name in favourite_languages.keys():
#    print(f"Hi {name.title()}")
#    if name in friends:
#        language = favourite_languages[name].title() # value of key
#        print(f"\t{name.title()}, I see you love {language}")
        
#    if 'erin' not in favourite_languages.keys():
#        print("Erin, please take our poll!")

for name in sorted(favourite_languages.keys()):
   print(f"{name.title()}, thank you for taking the poll.")

print("\n--------------------")

print("The following languages have been mentioned:")
for language in favourite_languages.values():
    print(language.title())

#no dublicates
print ( "'The following languages have been mentioned: ")
for language in set(favourite_languages.values()):
    print(language.title())