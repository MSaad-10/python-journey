"""
    What is Polymorphism?
        - The word comes from two Greek words:
            * Poly = Many
            * Morph = Forms
        - Polymorphism means 'one interface, many forms.'
        - The same method or operation behaves differently depending on the object that uses it.
    What is Duck Typing?
        - Python follows this idea: "If it walks like a duck and quacks like a duck, treat it like a duck."
        - Meaning: 
            * Python doesn't care what class an object belongs to.
            * It only cares does the object have the required method?
"""


# ============= Example 1 =============
class Dog:
    def sound(self):
        print('Bark')

class Cat:
    def sound(self):
        print('Meow')

class Cow:
    def sound(self):
        print('Moo')

animals = [Dog(), Cat(), Cow()]
for animal in animals:
    animal.sound()
print('*'*40)


# ============= Polymorphism Through Inheritance =============
''' Most commonly, polymorphism is achieved through method overriding. '''
class Animal:
    def sound(self):
        print('Animal Sound')

class Dog(Animal):
    def sound(self):
        print('Bark')

class Cat(Animal):
    def sound(self):
        print('Meow')

for animal in [Dog(), Cat()]:
    animal.sound()
print('*'*40)


# ============= Example 2 =============
class Shape:
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width
    
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        super().__init__(length, width)

    def area(self):
        return self.length * self.width

class Circle(Shape):
    PI = 3.14
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return self.PI * (self.radius**2)

shapes = [Rectangle(5.2, 6.7), Circle(5.6)]
for shape in shapes:
    print(f'Area:\t{shape.area()}')
print('*'*40)


# ============= Polymorphism Without Inheritance (Duck Typing) =============
''' Python doesn't require inheritance for polymorphism. '''
class Bird:
    def fly(self):
        print('Bird Flying')

class Airplane:
    def fly(self):
        print('Airplane Flying')

def start_flying(obj):
    obj.fly()

start_flying(Bird())
start_flying(Airplane())
print('*'*40)


# ============= Example 3 =============
class Dog:
    def speak(self):
        print('Bark')

class Robot:
    def speak(self):
        print('Hello World')

def make_sound(obj):
    obj.speak()

for obj in [Dog(), Robot()]:
    make_sound(obj)
print('*'*40)


# ============= Built-in Example of Polymorphism =============
''' The len() function. '''
print(len('Hello'))     # string
print(len([1,2,3]))     # list
print(len((1,2)))         # tuple

''' The + operator. '''
print(10 + 20)
print('Hello ' + 'World')
print([1,2] + [3,4])