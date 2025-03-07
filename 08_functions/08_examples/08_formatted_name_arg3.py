def get_formatted_name(first_name ,last_name, middle_name=''):
    if middle_name:
        fullname= f"{first_name.title()} {middle_name.title()} {last_name.title()}"
    else: 
        fullname= f"{first_name.title()} {last_name.title()}"

    return fullname

musician = get_formatted_name('john', 'saymon','richi')
print(musician)

musician = get_formatted_name(first_name= 'john', middle_name='saymon', last_name='richi')
print(musician)

