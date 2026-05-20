# create a file using x mode , it creates new file if not exist, if exist, it throws error.



#creates new txt file
y = open("file_hndl/files/hiii2.txt", "x")

y = open("file_hndl/files/hiii2.txt", "r")
print(y.read())

# throws error as it has already another file named hiii.txt
f = open("file_hndl/files/hiii.txt", "x")
y = open("file_hndl/files/hiii2.txt", "r")
print(f.read())



