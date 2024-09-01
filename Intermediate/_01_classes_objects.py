# Class
# a class is userdefined entity (datatype) that defines the type of data an object can contain
# and the action it can perform. It is template for creating objects.

class Employee:
    # common base class for all emoloyee or class attributes
    emp_count = 0
    # constructor
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        # modify class attributes
        Employee.emp_count +=1

    # methods
    def displayCunt(self):
        print ("Total employee in the organization %d"  %Employee.emp_count)

    def displayDetails(self, work_exp):
        print("Employee name:", self.name, "has salary:", self.salary, "and work experience is:", work_exp)

# object is instance of class, class can be called and passed required aruguments
emp1 = Employee("shiva", 50000)
emp1.displayCunt()
emp1.displayDetails(2)

# built-in class attributes
print("Employee.__doc__: ", Employee.__doc__)
print("Employee.__name__: ", Employee.__name__)
print("Employee.__module__: ", Employee.__module__)