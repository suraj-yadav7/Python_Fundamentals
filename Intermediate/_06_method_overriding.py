# Method Overriding
# The Python method overriding refers to defining a method in a subclass with the same name as a method in its superclass.
# In this case, the Python interpreter determines which method to call at runtime based on the actual object being referred to.

# Program of Parent Employee and subclass BackendDeveloper
class Employee:
    def __init__(self, nm, sal):
        self.name = nm
        self.salary = sal

    def getName(self):
        return self.name

    def getSalary(self):
        return self.salary

# Child class
class BackendDeveloper(Employee):
    def __init__(self, nm, sal, inc):
        super().__init__( nm, sal)
        self.increment = inc

    def getSalary(self):
        return self.salary+self.increment

# object of class
e1=Employee("karthik", 30000)
print("Salary of {} is {}".format(e1.getName(), e1.getSalary()))
be=BackendDeveloper("sandeep", 25000, 10000)
print("Backend developr {} salary after increment is {}: ".format(be.getName(), be.getSalary()))
