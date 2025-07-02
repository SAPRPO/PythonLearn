import getpass
import os.path
import sys
from pathlib import Path

from sympy import false

from whoami import Whoami

def test_get_user_name():
    username = getpass.getuser()
    username_test = Whoami.get_user_name()
    assert username ==username_test

def test_get_path_file_exists():
    path = os.getcwd()
    path=path+'/'+'4059352.csv'
    print(path)
    path_testing = Whoami.get_path('4059352.csv')
    assert path_testing == path

#def test_get_path_file_not_exists():
#    path = os.getcwd()
#    path=path+'/'+'xxx.csv'
#    print(path)
#    path_testing = Whoami.get_path('xxx.csv')
#    assert sys.exit(0)

def test_check_path_exist():
    p = os.getcwd()
    path = Path(p)
    Whoami.check_path(path)
    assert path.exists()

#def test_check_path_not_exist():
#    p = os.getcwd() + '/random'
#    path = Path(p)
#    Whoami.check_path(path)
#    assert not path.exists()