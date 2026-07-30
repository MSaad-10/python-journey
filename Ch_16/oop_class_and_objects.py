"""
    - Object-Oriented Programming (OOP) is a way of writing programs by organizing data and behavior into objects.
    - An object combines:
        * Data (attributes/properties) → What it has.
        * Behavior (methods/functions) → What it can do.
    - Python's OOP revolves around six major concepts:
        1. Class
        2. Object
        3. Encapsulation
        4. Inheritance
        5. Polymorphism
        6. Abstraction
"""


'''
    CLASS
    - A class is a blueprint or template for creating objects.
    - Think of it as the architectural plan of a house.
    - The blueprint isn't a house itself—it just describes how houses should be built.
'''


class Person:
    is_human = True         # class variable
    def __init__(self, first_name: str, last_name: str, age: int):
        # Instance Variables
        print('Constructor Initialized')
        self.first = first_name         # instance variable
        self.last = last_name
        self.age = age


P1 = Person('Muhammad', 'Saad', 21)
print(P1.first)
print(P1.last)
print(P1.age)
print()

P2 = Person('Muhammad', 'Abdullah', 12)
print(P2.first)
print(P2.last)
print(P2.age)