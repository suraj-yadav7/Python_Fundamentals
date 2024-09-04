# ABSTRACTION

# It refers to a programming approach by which only the relevant data about an object is exposed, hiding all the other details. 

# To create an abstract class in Python, it must inherit the ABC class that is defined in the ABC module.
from abc import ABC, abstractmethod
class Student(ABC):
    @abstractmethod
    def studentCount(self):
        section_A=30
        section_B=40
        total_count=section_A+section_B
        return total_count

    def top_marks(self):
        section_A_Mark=566
        section_B_Mark=580
        if(section_A_Mark>section_B_Mark): return section_A_Mark
        else: return section_B_Mark
# above method cannot be access directly , need to calling in super method way
# Abstract method overriding
class  Faculty(Student):
    def studentCount(self):
        return super().studentCount()

# instance of class faculty
f = Faculty()
# calling super methods
marks = f.top_marks()
print("Top marks: ", marks)
count = f.studentCount()
print("Student count: ", count)
