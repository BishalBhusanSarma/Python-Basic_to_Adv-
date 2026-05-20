# copy one file to another

import shutil
shutil.copy("file_hndl/files/intro.txt", "file_hndl/files/intro_copy.txt")
print("Copy file created")

# rename
import os
new_name = str(input("Enter file name: "))
file_n = "file_hndl/files/"+new_name+".txt"
os.rename("file_hndl/files/intro_copy.txt", file_n)
print("file renamed to "+ new_name+".txt")

# delete
import time

oldfile = open("file_hndl/files/oldfile.txt", "w")
print("file created for delete")

time.sleep(5)
os.remove("file_hndl/files/oldfile.txt")
print("file deleted")
