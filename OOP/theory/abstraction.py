#Abstraction is hiding the internal complexity and show the only essentials.


class avg:
    def __init__(self, numbers):
        self.numbers = numbers
    def aveg(self):
        sum = 0
        count = 0
        for i in self.numbers:
            sum += i
            count +=1

        average = sum/count
        print(average)
        print(count)

num = avg([45,54,65,67,8])        # we can only use the avg method, without much thinking about what 
num.aveg()                        # is going on in the backend, that is Abstraction.
