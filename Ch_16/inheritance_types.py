# ============= Types of Inheritance =============
# Single Inheritance
''' One parent → One child '''
class Animal:
    pass

class Dog(Animal):
    pass


# Multilevel Inheritance
''' Dog inherits from Mammal, which inherits from Animal. '''
class Animal:
    pass

class Mammal(Animal):
    pass

class Dog(Mammal):
    pass


# Multiple Inheritance
''' The child inherits from multiple parents. '''
class Father:
    pass

class Mother:
    pass

class Child(Father, Mother):
    pass


# Hierarchical Inheritance
''' One parent → Multiple children. '''
class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Lion(Animal):
    pass


# Hybrid Inheritance
''' A comibnation of two or more inheritance types. '''
class Animal:
    pass

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Bat(Bird, Mammal):    # Multiple Inheritance 
    pass


# ============= Multilevel Inheritance Example =============
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

class Smartphone(Phone):        # Child (Derived/Sub) class
    def __init__(self, brand_name: str, model_name: str, price: int, ram: str, rom: str, back_camera: str):
        super().__init__(brand_name, model_name, price)
        self.ram = ram
        self.rom = rom
        self.back_camera = back_camera

class FlagshipPhone(Smartphone):       # Child (Derived/Sub) class
    def __init__(self, brand_name: str, model_name: str, price: int, ram: str, rom: str, back_camera: str, front_camera: str):
            super().__init__(brand_name, model_name, price, ram, rom, back_camera)
            self.front_camera = front_camera

phone1 = Phone('Nokia', '3390', 100)
phone2 = Smartphone('Samsung', 'A52s', 5000, '8GB', '512GB', '50MP')
phone3 = FlagshipPhone('Apple', 'Iphone 11', 10000, '12GB', '1TB', '56MP', '32MP')
print(f'Phone1:\t{phone1.__dict__}')
print(f'Phone2:\t{phone2.__dict__}')
print(f'Phone3:\t{phone3.__dict__}')
print(f'Full Name:\t{phone3.full_name}')
print(f"Make Call:\t{phone2.make_a_call('123445666')}")
print('*'*40)