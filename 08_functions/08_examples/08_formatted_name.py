def get_formatted_name(first_name, last_name):
    fullname= f"{first_name.title()} {last_name.title()}"

    return fullname

musician = get_formatted_name('rob', 'halford')
print(musician)
