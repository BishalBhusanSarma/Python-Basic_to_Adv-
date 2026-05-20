# wrapping data + methods inside a single unit(class)

class amnt:
    def __init__(self, bal):
        self.__bal = bal #private 
    def sb(self):
        print(self.__bal) 

a = amnt(7888)

a.sb()