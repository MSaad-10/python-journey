"""
    What is raise?
        - raise is a Python keyword used to manually trigger an exception.
        - Instead of waiting for Python to detect a problem, you can tell Python: "This is an error—raise an exception."
        - You can raise different built-in exceptions depending on the situation.
        - Syntax:
            raise ExceptionType("Error message")
"""


# ============= 'raise' Stops Execution =============
print('Start')
# raise ValueError('Something went wrong!')
print('End')
print('*'*40)


# ============= Choosing the Correct Exception =============
def set_age(age: int):
    if not isinstance(age, int):
        raise TypeError('Age must be an integer')
    if age<0:
        raise ValueError('Age cannot be negative') 

set_age(-1)
print('*'*40)


# ============= Example 1 =============
def add(a,b):
    if isinstance(a, int) and isinstance(b, int):
        return a+b
    else:
        raise TypeError('Invalid data type')

print(add(1,'2'))
print('*'*40)


# ============= Example 2 =============
class InsufficientFundsError(Exception):                    # Custom Exception
    """Raised when a withdrawal exceeds the available account balance."""
    pass

def withdraw(balance: int, amount: int):
    if amount > balance:
        raise InsufficientFundsError(f"Cannot withdraw {amount} from balance of {balance}.")

    balance -= amount
    return balance

print(withdraw(1000, 5000))
print('*'*40)


# ============= Example 3 =============
def register(age: int):
    if age<18:
        raise ValueError('You must be at least 18')
    print('Registration Successful')

register(16)
print('*'*40)


# ============= Real-World Example 1 =============
class Animal:
    def __init__(self, name: str):
        self.name = name

    def sound(self):
        raise NotImplementedError('Implement this method in subclass')

class Dog(Animal):
    def __init__(self, name: str, breed: str):
        super().__init__(name)
        self.breed = breed

class Cat(Animal):
    def __init__(self, name: str, breed: str):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        return 'Meow Meow'

doggy = Dog('Jack', 'Pug')
# print(doggy.sound())          # NotImplementedError
cat = Cat('Slime', 'New')
print(cat.sound())
print('*'*40)


# ============= Real-World Example 2 =============
class Mobile:
    def __init__(self, name: str):
        self.name = name

class MobileStore:
    def __init__(self):
        self.mobiles = []

    def add_mobile(self, new_mobile):
        if isinstance(new_mobile, Mobile):
            self.mobiles.append(new_mobile.name)
        else:
            raise TypeError('new_mobile should be Mobile object')

phone1 = Mobile('Samsung S26')
store = MobileStore()
print(store.mobiles)
store.add_mobile(phone1)
print(store.mobiles)
# store.add_mobile('Iphone 17')     # TypeError
# print('*'*40)