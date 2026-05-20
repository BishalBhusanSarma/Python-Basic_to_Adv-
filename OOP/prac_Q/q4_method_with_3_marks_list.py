#create class Student that takes 3 marks and has a method average

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def average(self):
        sum = 0
        for i in self.marks:
            sum += i
        avg = sum/3
        print(avg)

s1 = Student("hii",[75,90,105])

s1.average()