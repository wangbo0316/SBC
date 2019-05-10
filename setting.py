import os
import sys
from datetime import datetime

PWD = os.getcwd()

def INSERT_PATH(path):
    a = os.path.join(PWD,path)
    for root, dirs, files in os.walk(a):
        sys.path.append(root)
    pass

MAIN_PATH = os.getcwd()

STATIC_PATH = MAIN_PATH + '\\Static'


DEFAULT_OPEN_PATH = "D:\\Data\\sme_bi\\" + datetime.now().strftime('%m%d')

