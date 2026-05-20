# open a file in w (write) mode

# This method replaces the file content if it already exist.
f = open("file_hndl/files/hiii.txt", "w")
f.write("hiiiiiii, I am old content. ") 
f = open("file_hndl/files/hiii.txt", "r")
print(f.read())


# This method will put the now thing into and without replacing to the original file.

nf = open("file_hndl/files/hiii.txt", "a")   # a defines append
nf.write("HI, I am new content. ")
with open("file_hndl/files/hiii.txt", "r") as nf:
    print(nf.read())


