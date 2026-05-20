
class hello:            #creating class
    x = "I am x"
    y = "i am y"
    z = "i am not x"

class pass_class:       # pass a class
    pass

p = hello()             # creating objects
q = pass_class()
# to 
# del p.y
# del p.x


print(p.x)
print(p.z)
print(p.y)
