#open a file


# Method-1
f = open("file_hndl/files/hiii.txt", "r")
print(f.read())
f.close() # need to close manually

# Method-2

with open("file_hndl/files/hiii.txt", "r") as a:
    
    print(a.read()) # closes automatically