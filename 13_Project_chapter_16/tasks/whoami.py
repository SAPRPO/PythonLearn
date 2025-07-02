import getpass, sys, os
from pathlib import Path
class Whoami:
    def __init__(self):
        print("Who i am?")

    @staticmethod
    def get_user_name():
        username = getpass.getuser()
        return username



    @staticmethod
    def get_path(f_name):
        p = os.getcwd()
        for dirpath, dirnames, filenames in os.walk(p):            
            if f_name in filenames:
                path = os.path.join(dirpath, f_name)
                print(path)                
                return path
        
        return sys.exit()


    

    
    @staticmethod
    def check_path(path):
        if path.exists():
            print(f"path {path} exists!")
        else:
            print(f"path {path} not exists!\nExit program")
            sys.exit()
