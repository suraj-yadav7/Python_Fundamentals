#Dynamic Binding
# In object-oriented programming, the concept of dynamic binding is closely related to polymorphism.
# In Python, dynamic binding is the process of resolving a method or attribute at runtime, instead of at compile time.

class Python:
    def specialFeature(self):
        print("Identity and membership operator")

class Javascript:
    def specialFeature(self):
        print("Async and await ")

class C:
    def specialFeature(self):
        print("compiled language and procedural language")

allObject = [Python(), Javascript(), C()]
for obj in allObject:
    obj.specialFeature()


# DUCK TYPING
# Another concept closely related to dynamic binding is duck typing. Whether an object is suitable for a particular use is
# determined by the presence of certain methods or attributes, rather than its type. This allows for greater flexibility & code reuse in Python.

class Circle:
    def draw(self):
        print("Circle is drawn")

class Square:
    def draw(self):
        print("Sqaure is drawn")

class rectangle:
    def draw(self):
        print("Recatangle is drawn")

class Triangle:
    def area(self):
        print("The area of a triangle is half the product of its base and height")

# duck typing method
# if obj don;t have this method will thorw error. it only need below mentioned.
def duck_typing(obj):
    obj.draw()

# instance
t=Triangle()
t.area()

objects=[Circle(), Square(), rectangle(), Triangle()]
for obj in objects:
    duck_typing(obj)