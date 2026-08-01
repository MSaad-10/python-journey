'''
    - A static method is a method that belongs to the class logically.
    - It does not need access to either the object (self) or the class (cls).
    - It behaves just like a normal function, except it is grouped inside the class because it is related to that class.
    - To define a static method, use the @staticmethod decorator.
'''


# ============= Basic Example =============
class Student:
    @staticmethod
    def greet():
        print('Welcome Students!')

student = Student()
student.greet()
print('*'*40)


# ============= Example: Utility Function =============
class Student:
    def __init__(self, name: str, age: int, marks: int):
        self.name = name
        self.age = age
        self.marks = marks

    @staticmethod
    def is_passing(marks):
        return marks >= 50

student1 = Student("Ali", 18, 43)
print(student1.__dict__)
print(student1.is_passing(43))
print()
student2 = Student('Asad', 23, 80)
print(student2.__dict__)
print(student2.is_passing(80))
print('*'*40)


# ============= Example: Mathematical Utilities =============
class Calculator:
    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b

    @staticmethod
    def multiply(a: int, b: int) -> int:
        return a * b

print(Calculator.add(5,3))
print(Calculator.multiply(5,3))
print('*'*40)


# ============= Can a Static Method Access Instance Variables? =============
class Student:
    def __init__(self, name: str):
        self.name = name

    # @staticmethod
    # def show():
# #         print(self.name)        # cannot access instance variable

# # s1 = Student('Ali')
# s1.show()


# ============= Can a Static Method Access Class Variables? =============
class Student:
    university = "UET Lahore"

    @staticmethod
    def show():
        print(Student.university)       # can't access directly using 'cls', have to reference the class name explicitly

student = Student()
student.show() 
print('*'*40)


# ============= Complete Example: @classmethod, @staticmethod, instance method =============
class Student:
    university = "UET Lahore"

    def __init__(self, name: str, marks: int):
        if not self.is_valid_marks(marks):
            raise ValueError(f"Invalid marks score: {marks}")
        self.name = name

    # Instance Method
    def display(self):
        print(self.name)

    # Class Method
    @classmethod
    def show_university(cls):
        print(cls.university)

    # Static Method
    @staticmethod
    def is_valid_marks(marks: int) -> bool:
        return 0 <= marks <= 100

student = Student('Saad', 100)
student.display()
Student.show_university()
print(student.is_valid_marks(10))
print('*'*40)