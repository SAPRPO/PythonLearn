def get_formatted_name(first_name, last_name):
    fullname= f"{first_name.title()} {last_name.title()}"
    return fullname.title()

while True:
    print("\nPlease tell your name:")
    f_name= input("First name: ")
    if f_name == 'q':
        break
    l_name= input("Last name: ")
    if l_name == 'q':
        break
formatted_name = get_formatted_name(f_name, l_name)
print(formatted_name)