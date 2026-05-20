class init_implimentation:
    def __init__(self, name="default", age = 18, location= "GHY", jobrole="Studtnt"):
        self.name = name
        self.age = age
        self.location = location
        self.jobrole = jobrole

    


p = init_implimentation()

print(p.name)
print(p.age)
print(p.location)
print(p.jobrole)