# Encapsulation
# Encapsulation is the process of bundling attributes and methods within a single unit.
class Student:
    def __init__(self, name="Rajkumar", marks=50):
        self.name = name
        self.marks = marks

s1 = Student()
s2 = Student("Binod", 25)

print ("Name: {} marks: {}".format(s1.name, s2.marks))
print ("Name: {} marks: {}".format(s2.name, s2.marks))

class Employee:
    def __init__(self, name="Rajesh", project=50):
        self.__name = name
        self.__project = project

    def studentdata(self):
        print ("Name: {} Poeject: {}".format(self.__name, self.__project))

s1 = Employee()
s2 = Employee("Bharat", 5)
s1.studentdata()
s2.studentdata()

