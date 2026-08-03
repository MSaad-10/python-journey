'''
    - @property and @<property_name>.setter decorators are among the most "Pythonic" features in OOP. 
    - They allow you to control access to attributes while making them look like normal variables.
    - They replace the traditional getter() and setter() methods that are used in other langauges.
    - @property converts a method into a read-only attribute.
    - Without them:
        student.get_marks()
        student.set_marks(90)
    - With them:
        print(student.marks)
        student.marks = 90
    - Even though Python is secretly calling methods behind the scenes.
'''


# ============= Example: setting and getting marks =============
class Student:
    def __init__(self):
        self._marks = 95

    @property           # Getter(): makes '_marks' read only if setter is not defined
    def marks(self):
        return self._marks

    @marks.setter       # Setter(): getter() must be before the setter() to create it
    def marks(self, new_marks):
        if 0 <= new_marks <= 100:
            self._marks = new_marks
        else:
            raise ValueError(f'Invalid marks: {new_marks}')

student = Student()
print(f'Old Marks:\t{student.marks}')    # Pythonic way instead of calling getter() and setter() methods
student.marks = 100
print(f'New Marks:\t{student.marks}')
print('*'*40)


# ============= Read-Only Property =============
class Student:
    def __init__(self):
        self._marks = 50

    @property           # makes 'marks' read-only because setter is not defined
    def marks(self):
        return self._marks

student = Student()
print(f'Marks:\t\t{student.marks}')
# student.marks = 100     # AttributeError
print('*'*40)


# =============  Read-Write Property =============
class Student:
    def __init__(self):
        self._marks = 50

    @property           
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, new_marks: int):
        if new_marks >=0:
            self._marks = new_marks
        else: 
            raise ValueError(f'Invalid marks: {new_marks}')

student = Student()
print(f'Old Marks:\t{student.marks}')
student.marks = 100   
print(f'New Marks:\t{student.marks}')
# student.marks = -1    # ValueError
print('*'*40)


# ============= Property with Calculations ============
''' Properties aren't limited to stored values. '''
class Rectangle:
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    @property
    def area(self):
        print('Calculating...')
        return self.length * self.width

r = Rectangle(5.4, 4.6)
print(f'Area:\t\t{r.area}')
print('*'*40)


# ============= Property Deleter =============
''' This allows controlled deletion of an attribute. '''
class Student:
    def __init__(self):
        self._marks = 100

    @property
    def marks(self):
        return self._marks

    @marks.deleter
    def marks(self):
        del self._marks
        print(f'marks deleted!!')

student = Student()
print(f'Marks:\t\t{student.marks}')
del student.marks
# print(student.marks)  # AttributeError
print('*'*40)


# ============= Real-World Example =============
''' Without @property and setter decorator we have 3 problems in our code '''
class Phone:
    def __init__(self, brand_name: str, model_name: str, price: int):
        self.brand = brand_name
        self.model = model_name
        self._price = price
        self.complete_specification = f'{self.brand} {self.model} and price is {self._price}'

    def make_a_call(self, phone_number: str):
        print(f'calling {phone_number}')

    def full_name(self):
        return f'{self.brand} {self.model}'

phone1 =  Phone('Nokia', '1100', -1000)     # P1: passing -ve value in conctructor
print(phone1.brand)
print(phone1.model)
phone1._price = -500          # P2: setting a -ve value in a variable
print(phone1._price)
print(phone1.complete_specification)    # P3: value not updated in this variable
print('*'*40)


''' Solution: By using @property and setter decorators '''
class Phone:
    def __init__(self, brand_name: str, model_name: str, price: int):
        self.brand = brand_name
        self.model = model_name
        self.price = price      # routes through the setter automatically

    @property # Getter()
    def complete_specification(self) -> str:
        return f'{self.brand} {self.model} and price is {self._price}'

    # Getter() for price
    @property
    def price(self):
        print('Price getter() called!!')
        return self._price

    # Setter() for price
    @price.setter
    def price(self, new_price: int):
        print('Price setter() called!!')
        if new_price >= 0:
            self._price = new_price
        else:
            raise ValueError(f"Invalid Price {new_price}")

    def make_a_call(self, phone_number: str):
        print(f'calling {phone_number}')

    def full_name(self):
        return f'{self.brand} {self.model}'

phone1 =  Phone('Nokia', '1100', 100)     
print(phone1.brand)
print(phone1.model)
phone1.price = 500
print(phone1.price)
print(phone1.complete_specification)        # use as a variable  