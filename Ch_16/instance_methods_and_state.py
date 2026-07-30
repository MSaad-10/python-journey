"""
    - An instance method is a method that works with a specific object (instance) of a class.
    - It can:
        * Access the object's attributes.
        * Modify the object's attributes.
        * Call other instance methods.
    - Every instance method has self as its first parameter.
"""


# ============= Basic Usage =============
class Person:
    def __init__(self, first_name: str, last_name: str, age: int):
        print('Constructor Initialized')
        self.first = first_name
        self.last = last_name
        self.age = age

    def full_name(self):
        return f"{self.first} {self.last}"

    def is_adult(self):
        return self.age>=18

    def display(self):
        print(f'First Name:\t{self.first}')
        print(f'Last Name: \t{self.last}')
        print(f'Full Name: \t{self.full_name()}')   # calls other instance method
        print(f'Age:       \t{self.age}')
        print(f'Is Adult: \t{self.is_adult()}')


P1 = Person('Muhammad', 'Saad', 21)
print(P1.full_name())
print(P1.is_adult())
print(Person.is_adult(P1))      # same as above
P1.display()
print()

P2 = Person('Muhammad', 'Ahmad', 18)
print(P2.full_name())
print(P2.is_adult())
print(Person.is_adult(P2))     # same as above
P2.display()
print()
print('*'*40, '\n')


# ============= Instance Methods Can Modify Object Data =============
class BankAccount:
    def __init__(self, balance: int):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds for this withdrawal.")
        self.balance -= amount


account = BankAccount(1000)
account.deposit(500)
account.withdrawal(800)
# account.withdrawal(8000)
print(account.balance)
print()
print('*'*40, '\n')