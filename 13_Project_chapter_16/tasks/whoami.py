import getpass, sys
class Whoami:
    def __init__(self):
        print("Who i am?")

    @staticmethod
    def get_user_name():
        username = getpass.getuser()
        return username

    @staticmethod
    def check_path(path):
        if path.exists():
            print(f"path {path} exists!")
        else:
            print(f"path {path} not exists!")
            sys.exit()
