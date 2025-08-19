import os as o
import shutil
try:
    # o.remove('D:/python-may-2025/file-handling/demofolder')
    shutil.rmtree('D:/python-may-2025/file-handling/demofolder')
    print('File deletion succesful')
except FileNotFoundError as e:
    print(e)