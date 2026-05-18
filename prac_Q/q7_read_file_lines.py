#read file data line by line


# Read lines one by one

print("It shows how to print lines one by one from a txt file")
with open("file_hndl/files/lines.txt", "r") as l:
    line1 = l.readline()
    line2 = l.readline()
    line3 = l.readline()
    line4 = l.readline()
    line5 = l.readline()

    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)


# read all lines. It returns list of lines.

print("It shows how to print all lines")

with open("file_hndl/files/lines.txt", "r") as l:
    lineall = l.readlines()
    print(lineall)


# print the first line
print("\nthe first line is: ")
print(lineall[0])

# no of lines present in the file

print("No. of files that present in the file is: ", len(lineall))