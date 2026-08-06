"""
    Types of Polymorphism
        - In general OOP theory, there are two main types of polymorphism:
            * Compile-Time (Static) Polymorphism
            * Run-Time (Dynamic) Polymorphism
        - However, Python mainly supports Runtime Polymorphism because it is a dynamically typed language.

    Compile-Time Polymorphism (Static Polymorphism)
        - The method to execute is decided before the program runs, i.e., during compilation.
        - Languages like C++ and Java support this through method overloading.
        
    Runtime Polymorphism (Dynamic Polymorphism)
        - The method is selected while the program is running.
        - Python mainly supports this using method overriding and duck typing.
"""


# ============= Does Python Support Compile-Time Polymorphism?  =============
''' No, not in the traditional sense. '''
class Calculator:
    def add(self, a, b):
        return sum(a,b)

    def add(self, a, b, c):
        return a+b+c

calc = Calculator()
# print(calc.add(1,2))        # TypeError: The first method is overwritten.
print(calc.add(1,2,3))      # Only the second add(self, a, b, c) exists.
print('*'*40)


# ============= How Python Achieves Similar Behavior =============
''' Instead of method overloading, Python uses: '''
# Default Arguments
class Calculator:
    def add(self, a, b, c=0):
        return a+b+c

calc = Calculator()
print(calc.add(5,3))
print(calc.add(5,3,5)) 

# Using *args
class Calculator:
    def add(self, *numbers):
        return sum(numbers)

calc = Calculator()
print(calc.add(2, 3))
print(calc.add(2, 3, 4))
print(calc.add(2, 3, 4, 5))
print('*'*40)


# ============= Example: Runtime Polymorphism =============
class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

for animal in [Animal(), Dog(), Cat()]:
    animal.sound()
print('*'*40)


# ============= Runtime Polymorphism Using Duck Typing =============
''' Inheritance is not even required. '''
class Bird:
    def fly(self):
        print("Bird Flying")

class Airplane:
    def fly(self):
        print("Airplane Flying")

def start_flying(obj):
    obj.fly()

for obj in [Bird(), Airplane()]:
    start_flying(obj)
print('*'*40)