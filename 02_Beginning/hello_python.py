message = "hello world" 
print(message)

#strings

print(message.title())

#variables in strings

first_name = "ilia"
last_name = "uriupin"
full_name = f"{first_name} {last_name}"
print(f"Hello,\n\t{full_name.title()}")


#delete space_symbols

favorite_language = ' python '
print(favorite_language)
print(favorite_language.rstrip()) # delete spaces right
print(favorite_language.lstrip()) # delete spaces left


#remove prefixes (url prefixes)

no_prefix = 'https://ya.ru'
n_pr = no_prefix.removeprefix('https://')

print(no_prefix)
print(n_pr)