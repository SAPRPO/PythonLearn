import getpass, sys
from pathlib import Path
class Whoami:
    def __init__(self):
        print("Who i am?")

    @staticmethod
    def get_user_name():
        username = getpass.getuser()
        return username

    @staticmethod
    def get_path():
        p = Path().absolute() 
        #rp =Path.relative_to()
        #try relative filepath use 
        return p

    @staticmethod
    def check_path(path):
        if path.exists():
            print(f"path {path} exists!")
        else:
            print(f"path {path} not exists!\nExit program")
            sys.exit()
