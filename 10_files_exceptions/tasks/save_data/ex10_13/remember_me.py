from pathlib import Path
import json

relative_filepath= '10_files_exceptions/tasks/save_data/ex10_13/'


def get_user_info(path):
    #print("read username")
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info
    else:
        return None
    
def write_user_info(path):
    #print("Write username")
    username = user_name()
    userage = user_age()
    usercity = user_city()

    user_info = {
        'username' : username,
        'userage' : userage,
        'usercity' : usercity,
    }
    #print(user_info)
    contents = json.dumps(user_info)
    path.write_text(contents)
    return username

def user_name():
   # user_name= input("What is your name? ")
   # return user_name

    return input("What is your name? ")

def user_age():
    user_age = input("Your age: ")
    return user_age

def user_city():
    user_city = input("Your city: ")
    return user_city

def format_output(userinfo):
    #format output info
    user_info_output = ''
    for k, v in userinfo.items():
        user_info_output += f'{k} : {v}\n'

    return user_info_output



def greet_user():
    path = Path(f'{relative_filepath}username.json')
    userinfo = get_user_info(path)
    if userinfo:
        user_info_output = format_output(userinfo)
        print(f"User name info:\n{user_info_output}")
        
    else:
        userinfo = write_user_info(path)
        user_info_output = format_output(userinfo)
        print(f'We will remember you:\n {user_info_output}')

greet_user()