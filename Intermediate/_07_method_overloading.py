# Method Overloading
# Method overloading is a feature of object-oriented programming where a class can have
# multiple methods with the same name but different parameters.

# Python by default don't support method overloading. But can be done alternative way.

# progam
class AirthmeticOperation:
    def add(self, a, b):
        sum = a+b
        return sum

    def add(self, a, b,c):
        sum = a+b+c
        return sum
obj = AirthmeticOperation()
addition=obj.add(10,20, 30)
print("addition: ", addition)
# throw error in python
# addition2 = obj.add(5, 5)
# print("Calling first method: ", addition2)

# implementing method overloading using  multipledispatch
from multipledispatch import dispatch

class SumOperation:
    @dispatch(int, int)
    def add(self, a, b):
        x = a+b
        return x

    @dispatch(int, int, int)
    def add(self, a, b, c):
        y=a+b+c
        return y

    @dispatch(int)
    def add(self, a):
        z=a+20
        return z

so = SumOperation()
result = so.add(7, 7)
print("Result two parameter: ", result)

result2 = so.add(3, 7, 5)
print("Result three parametes: ", result2)