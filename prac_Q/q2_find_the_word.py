# find a ford from the txt file we read.

f= open("file_hndl/files/hiii.txt")
data_txt = f.read().lower()
word = "tun"
if word in data_txt:
    print("yes, your file contains the word: " + word)
else:
    print("No")