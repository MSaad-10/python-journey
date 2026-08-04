"""
    - Inheritance is the process by which one class acquires the properties (attributes) and behaviors (methods) of another class.
    - In simple words, A new class can reuse the code of an existing class and also add its own new features.

"""


# ============= Basic Example =============
class Animal:
    def eat(self):
        print('Eating...')

    def sleep(self):
        print('Sleeping...')

class Dog(Animal):
    pass

dog = Dog()
dog.eat()       # inherits from Animal class
dog.sleep()
print('*'*40)


# ============= Adding New Features =============
''' The child class can also have its own methods. '''
class Animal:
    def eat(self):
        print('Eating...')

    def sleep(self):
        print('Sleeping...')

class Dog(Animal):
    def bark(self):
        print('Barking...')

dog = Dog()
dog.eat()
dog.sleep()
dog.bark()
print('*'*40)


# ============= Constructor Inheritance =============
''' The Child class automatically inherits the Parent class' constructor. '''
class Animal:
    def __init__(self, name: str):
        self.name = name

class Dog(Animal):
    pass

dog = Dog('Mark')
print(dog.name)
print('*'*40)


# ============= Child Constructor =============
class Animal:
    def __init__(self, name: str):
        self.name = name

class Dog(Animal):
    def __init__(self, name: str, breed: str):
        super().__init__(name)                  # super() lets the child class call methods of its parent.
        self.breed = breed

dog = Dog('Tommy', 'Labrador')
print(dog.name)     # comes from Animal
print(dog.breed)    # comes from Dog
print('*'*40)


# ============= Method Overriding =============
''' The child class can replace a parent's method. Python always prefers the child's version if it exists. '''
class Animal:
    def sound(self):
        print('Some Sound')

class Dog(Animal):
    def sound(self):
        print('Bark')

dog = Dog()
dog.sound()
animal = Animal()
animal.sound()
print('*'*40)


# ============= Calling the Parent Method =============
class Animal:
    def sound(self):
        print('Some Sound')

class Cat(Animal):
    def sound(self):
        super().sound()
        print('Meow')

cat = Cat()
cat.sound()
animal = Animal()
animal.sound()
print('*'*40)


# ============= Example: Phone and Smartphone Class =============
class Phone:            # Parent (Base/Super) class
    def __init__(self, brand_name: str, model_name: str, price: int):
        self.brand = brand_name
        self.model = model_name
        self.price = price

    @property
    def full_name(self) -> str:
        return f"{self.brand} {self.model}"

    @property
    def price(self) -> int:
        return self._price

    @price.setter
    def price(self, new_price: int):
        if new_price >= 0:
            self._price = new_price
        else:
            raise ValueError(f"Invalid Price: {new_price}")

    def make_a_call(self, number: str) -> str:
        return f"Calling... {number}"

class Smartphone(Phone):        # Child (Derived, Sub) class
    def __init__(self, brand_name: str, model_name: str, price: int, ram: str, rom: str, camera: str):
        super().__init__(brand_name, model_name, price)
        self.ram = ram
        self.rom = rom
        self.camera = camera

phone1 = Phone('Nokia', '3390', 100)
phone2 = Smartphone('Samsung', 'A52s', 5000, '8GB', '512GB', '50MP')
print(phone1.__dict__)
print(phone2.__dict__)
print('*'*40)