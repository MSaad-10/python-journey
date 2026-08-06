"""
    - Operator Overloading means giving existing Python operators (+, -, *, ==, <, etc.) a new meaning for user-defined objects.
    - In simple words:
        * Normally, operators work with built-in data types like int, float, and str.
        * Operator overloading allows your own classes to use these operators in a meaningful way.
"""


# ============= Example 1: Overloading + =============
class Number:
    def __init__(self, value: int):
        self.value = value

    def __add__(self, other):
        if isinstance(other, Number) or isinstance(other, int):
            return self.value + other.value
        return NotImplemented

n1 = Number(10)
n2 = Number(20)
print(n1 + n2)      # n1.__add__(n2)
print('*'*40)


# ============= Returning an Object =============
''' Instead of returning an integer, we can return another Number object. '''
class Number:
    def __init__(self, value: int):
        self.value = value

    def __add__(self, other):
        if isinstance(other, Number) or isinstance(other, int):
            return Number(self.value + other.value)
        return NotImplemented

    def __str__(self):
        return str(self.value)

n1 = Number(5)
n2 = Number(15)
result = n1 + n2    # n1.__add__(n2)
print(result)       # 'result' is a 'Number' object not 'int'
print('*'*40)


# ============= Example 2: Overloading - =============
class Number:
    def __init__(self, value: int):
        self.value = value

    def __sub__(self, other):
        return self.value - other.value

a = Number(15)
b = Number(20)
print(a - b)    # a.__sub__(b)
print('*'*40)


# ============= Example 3: Overloading * =============
class Number:
    def __init__(self, value: int):
        self.value = value

    def __mul__(self, other) -> int:
        return self.value * other.value

a = Number(5)
b = Number(3)
print(a * b)       # a.__mul__(b)
print('*'*40)


# ============= Example 4: Overloading == =============
class Student:
    def __init__(self, marks: int):
        self.marks = marks

    def __eq__(self, other):
        return self.marks == other.marks

s1 = Student(100)
s2 = Student(10)
print(s1 == s2)
print('*'*40)


# ============= Example 5: Overloading < =============
class Student:
    def __init__(self, marks: int):
        self.marks = marks

    def __lt__(self, other):
        return self.marks < other.marks

student1 = Student(80)
student2 = Student(90)
print(student1 < student2)
print('*'*40)


# ============= Example 5: Overloading > =============
class Student:
    def __init__(self, marks: int):
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks

student1 = Student(80)
student2 = Student(90)
print(student1 > student2)
print('*'*40)


# ============= Real-Life Example =============
class Cart:
    def __init__(self, items):
        self.items = items

    def __add__(self, other):
        return Cart(self.items + other.items)
    
    def __str__(self):
        return str(self.items)

cart1 = Cart(['Laptop'])
cart2 = Cart(['Mouse'])
cart3 = cart1 + cart2
print(cart3)
print('*'*40)


# ============= Other Common Operator Methods =============
'''
    Operator                        Magic Method
    /                               __truediv__()
    //                              __floordiv__()
    %                               __mod__()
    **                              __pow__()
    !=                              __ne__()
    <=                              __le__()  
    >=                              __ge__()
''' 