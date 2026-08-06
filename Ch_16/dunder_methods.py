"""
    - Magic methods are special methods whose names start and end with double underscores.
    - Dunder = Double UNDERscore (__method__)
    - These methods make your custom objects behave like Python's built-in objects.
    - Python automatically calls these methods when you perform certain operations.
"""


# ============= Example 1: __init__() =============
class Student:
    def __init__(self, name: str):
        self.name = name

student = Student('Asad')
student.__init__('Asad')    # Python secretly does this, you never call it yourself.


# ============= Example 2: __str__() =============
''' __str__() controls what is displayed when you print an object. '''
class Student:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"Student Name:\t{self.name!r}"      # !r adds single quotes around the called instance

class Teacher:
    def __init__(self, name: str):
        self.name = name

student = Student('Saad')
print(student.__str__())    # With defined __str__() method in class    
teacher = Teacher('Ali')
print(teacher.__str__())    # Without defining __str__() method in class
print('*'*40)


# ============= Example 3: __len__() =============
class Playlist:
    def __init__(self):
        self.songs = ['A', 'B', 'C', 'D']

    def __len__(self):
        return len(self.songs)

class Movie:
    def __init__(self):
        self.time_stamps = ['2:00', '14:21', '1:32:12']

    def __len__(self) -> int:
        return len(self.time_stamps) 

playlist = Playlist()
print(len(playlist))    # With defined __len__() method in class
movie = Movie()
print(len(movie))
print('*'*40)


# # ============= Example 4: __add__() =============
# ''' Suppose you want to use the + operator with your objects. '''
class Number:
    def __init__(self, value: int):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

a = Number(10)
b = Number(20)
print(a + b)
a.__add__(b)    # Python internally calls
print('*'*40)


# ============= Example 5: __eq__() =============
''' Python compares object identities (memory addresses), not their contents. '''
class Student:
    def __init__(self, name: str):
        self.name = name

s1 = Student('Saad')
s2 = Student('Saad')
print(s1 == s2)     # different objects
print(s1 == s1)     # same objects

# Customize it
class Student:
    def __init__(self, name: str):
        self.name = name

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Student):      # Try the code for different class object by commenting out this validation 
            return NotImplemented
        return self.name == other.name

s1 = Student('Ali')
s2 = Student('Ali')
s3 = Number(20)
print(s1 == s2)
print(s3 == s1)    # Two different class' objects
print('*'*40)


# ============= Example 6: __repr__() ============= Representation
''' __repr__() returns the official string representation of an object. '''
class Student:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self) -> str:
        return f"Student('{self.name}')"

class Animal:
    def __init__(self, name: str):
        self.name = name        

student = Student('Saad')
print(repr(student))        # with __repr__() method
animal = Animal('Lion')
print(repr(animal))         # without __repr__() method
print('*'*40)


# ============= Difference between __str__() and __repr__() =============
'''
    __str__()       Human-readable representation
    __repr__()      Developer/debug representation 
'''
class Student:
    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return f"Student: {self.name}"

    def __repr__(self) -> str:
        return f"Student('{self.name}')"

student1 = Student('Saad')
print(student1)
print(repr(student1))
print('*'*40)


# ============= Real-Life Example =============
class Cart:
    def __init__(self):
        self.items = []

    def __len__(self) -> int:
        return len(self.items)

    def __str__(self) -> str:
        return f"Cart has {len(self.items)} items"

cart = Cart()
cart.items.append('Laptop')
cart.items.append('Mouse')
cart.items.append('Keyboard')
print(cart)                     # cart.__str__()
print(len(cart))                # cart.__len__()
print('*'*40)