# Inheritance is one of the most important features of object-oriented programming languages like Python.
# It is used to inherit the properties and behaviours of one class to another.
# The class that inherits another class is called a child class & class that gets inherited is called a base or parent class.

# parent class
class Parent:
    def parentMethod(self):
        print("Parent method of parent class")

# child class
class Child(Parent):
    def childMethod(self):
        print("Calling child method")

# parent class
c = Child()
c.childMethod()
# calling parent methods
c.parentMethod()

# multiple inheritance
class Addition:
    def __init__(self, a, b):
        self.val = a
        self.val2 = b
    def sum(self):
        return self.val+self.val2

class Subtraction:
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b
    def sub(self):
        return self.num1 - self.num2

class Operation(Addition, Subtraction):
    def __init__(self, a, b):
        Addition.__init__(self, a, b)
        Subtraction.__init__(self, a, b)
    def sum_and_sub(self):
        sumResult = self.sum()
        subResult = self.sub()
        return (sumResult, subResult)

# calling parent methods from child
obj = Operation(10,20)
print("Additon of Parent method: ", obj.sum())
print("Subtraction of Parent method: ", obj.sub())
print("Both methods: ", obj.sum_and_sub())