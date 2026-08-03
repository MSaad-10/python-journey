'''
    ENCAPSULATION
        - Bundling (combining) data (attributes) and the methods (functions) that operate on that data into a single unit (class), while controlling how that data is accessed or modified.
        - In simple words:
            * Keep data and related methods together.
            * Protect important data from being modified incorrectly.
        - Encapsulation has two ideas:
            * Bundling:     Keep data and methods together.
            * Data Hiding:  Prevent direct access to important data. Python provides naming conventions for this. 
                -- Public Members          -- Proteted Members             -- Private Members         
'''


# ============= Without Encapsulation =============
class BankAccount:
    def __init__(self, balance: int):
        self.balance = balance

account = BankAccount(1000)
account.balance = -5000     # Anyone can set an invalid balance
print(account.balance)
print('*'*40)


# ============= With Encapsulation =============
class BankAccount:
    def __init__(self, balance: int):
        self.__balance = balance    # 'balance' is private member

    def deposit(self, amount: int):
        self.__balance += amount

    def withdraw(self, amount: int):
        if amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
# print(account.__balance)        # cannot access directly
account.withdraw(700)
print(account.get_balance())    
print('*'*40)


# ============= Bundling =============
class Student:
    def __init__(self, name: str):
        self.name = name

    def display(self):
        print(self.name)

student = Student('Saad')
print(student.name)
student.display()
print('*'*40)


# ============= Data Hiding =============
# Public Members
class Student:
    def __init__(self):
        self.name = "Hamza"

public_student = Student()
print(public_student.name)     # can be accessed
public_student.name = "Ali"    # can be changed
print(public_student.name)
print('*'*40)

# Protected Members (Convention)     -> A convention, not an enforcement
class Student:
    def __init__(self):
        self._marks = 95    # _ means this is intended for internal use only.

protected_student = Student()
print(protected_student._marks)   # can be accessed
protected_student._marks = 100    # can be changed
print(protected_student._marks)  

# Private Members
class Student:
    def __init__(self):
        self.__marks = 87   # __ means this is private and it cannot be changed & accessed

private_student = Student()
# print(private_student.__marks)      # AttributeError because python performs 'name mangling'
print('*'*40)


# ============= Name Mangling =============
"""
    - Python changes 'self.__marks' to '_Student__marks' internally.
    - Thus, Python is discouraging accidental access, not providing absolute security. 
"""

class Student:
    def __init__(self):
        self.__marks = 35

mangled_student = Student()
print(mangled_student.__dict__)
print(mangled_student._Student__marks)      # can be accessed by using mangled attribute name
print('*'*40)


# ============= Accessing Private Variables =============
# Inside Class
class Student:
    def __init__(self):
        self.__marks = 95

    def show(self) -> int:
        return self.__marks     # class can access its own private data

student = Student()
print(student.show())
print('*'*40)

# Getters: A getter returns a private value.
class Student:
    def __init__(self):
        self.__marks = 96

    def get_marks(self) -> int:
        return self.__marks

student = Student()
print(student.get_marks())
print('*'*40)

# Setters: A setter changes a private value safely.
class Student:
    def __init__(self):
        self.__marks = 97

    def set_marks(self, marks: int):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            raise ValueError("Invalid Value!")

student = Student()
student.set_marks(100)     # now invalid values can be rejected