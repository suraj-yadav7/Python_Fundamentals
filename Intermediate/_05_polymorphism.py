# he term polymorphism refers to a function or method taking different forms in different contexts.
# There are four ways to implement polymorphism in Python − Duck typing, Operator Overloading, Method Overloading, Method Overriding.
class Duck:
    def sound(self):
        return "Quack, quack!"

class AnotherBird:
    def sound(self):
        return "I'm similar to a duck!"

def makeSound(duck):
    print(duck.sound())

# creating instances
duck = Duck()
anotherBird = AnotherBird()
# calling methods
makeSound(duck)
makeSound(anotherBird)

# Method Overriding in Python
from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def draw(self):
        "Abstract method"
        return

class circle(shape):
    def draw(self):
        super().draw()
        print ("Draw a circle")
        return

class rectangle(shape):
    def draw(self):
        super().draw()
        print ("Draw a rectangle")
        return

shapes = [circle(), rectangle()]
for shp in shapes:
    shp.draw()