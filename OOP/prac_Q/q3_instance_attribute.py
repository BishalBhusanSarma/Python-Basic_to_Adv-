# create instance atttribute.


class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

Student1 = Student("Hiii", "BCA")
Student2 = Student("Byeee", "MCA")

print("Student 1:")

print(Student1.name)
print(Student1.course)
print("\nStudent 2:")
print(Student2.name)
print(Student2.course)



class fooditem:
    category = "SNACKS" #class attribute
    def __init__(self, name ):
        self.name = name # instance attribute

F1 = fooditem("Samosa")
F2 = fooditem("gulabjaamun")

print(F1.category)
print(F1.name)
print(F2.category)
print(F2.name)