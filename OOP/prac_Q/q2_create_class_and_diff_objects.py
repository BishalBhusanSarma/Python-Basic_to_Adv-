# create a class laptop and make two different objects

class Laptop:
    def __init__(self):
        print("I am Laptop class containing default values.")

    brand = "default"
    ram = "8 GB"
    price = 200000


L1 = Laptop()
L1.brand = "MAC"
print(L1.brand)
print(L1.ram)
print(L1.price, "/-")


L2 = Laptop()
L2.price = 1345636
print(L2.brand)
print(L2.ram)
print(L2.price, "/-")