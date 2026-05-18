# checks wheather a file is exist or not 

import os

f_path = "file_hndl/files/hiii.txt"

if os.path.isfile(f_path):
    print("File exists")
else:
    print("NO")