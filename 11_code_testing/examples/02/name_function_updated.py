
#def get_formatted_name(first, middle,last): #
def get_formatted_name(first,last,  middle = ''): # not fail
    if middle:
        full_name= f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

