# create a file named "intro.txt", add your personal details and append your 3 goals for this month in the file.


# creating file "intro.txt" and adding details.

intro =  open("file_hndl/files/intro.txt", "w")
intro = intro.write("Hello, I am bishal.\nI love Bikes and Boobies.\nI am just a mechanic that knows nothing.\nIDK what to say.\nMaza aa rha hain likh k.\n")

append_intro = open("file_hndl/files/intro.txt", "a")
append_intro = append_intro.write("My three goals are- \n1. I want to be fukin rich.\n2. I want to be richer.\n3. I want to be richest.")

with open("file_hndl/files/intro.txt", "r") as intr:
    print(intr.read())
