'''
    - Method Resolution Order (MRO) is the order in which Python searches classes to find a method or attribute.
    - In other words, MRO is the path Python follows to look for a method or attribute.
'''


# ============= Rule 1: Python searches from left to right =============
class Father:
    def show(self):
        print('Father')

class Mother:
    def show(self):
        print('Mother')

class Child(Father, Mother):
    pass

child = Child()
child.show()        # whose show() will be called?
print(f'MRO:\t{Child.__mro__}')
print('*'*106)


# ============= Rule 2: Stop at the First Match =============
class Animal:
    def eat(self):
        print('Animal Eating')

class Dog(Animal):
    pass

dog = Dog()
dog.eat()
print(f'MRO:\t{Dog.__mro__}')
print('*'*106)


# ============= Example 1: Method Overriding =============
class Animal:
    def sound(self):
        print('Animal Sound')

class Cat(Animal):
    def sound(self):
        print('Meow')

cat = Cat()
cat.sound()
print(f'MRO:\t{Cat.__mro__}')
print('*'*106)


# ============= MRO in Multilevel Inheritance =============
class Animal:
    def eat(self):
        print('Eating')

class Mammal(Animal):
    pass

class Zebra(Mammal):
    pass

zebra = Zebra()
zebra.eat()
print(f'MRO:\t{Zebra.__mro__}')
print('*'*106)


# ============= MRO in Hierarchical Inheritance =============
class Animal:
    def sleep(self):
        print('Sleeping')

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()
dog.sleep()
print(f'MRO:\t{Dog.__mro__}')
print('*'*106)


# ============= MRO in Multiple Inheritance =============
class A:
    def show(self):
        print('A')

class B:
    def show(self):
        print('B')

class C(A,B):
    pass

c = C()
c.show()
print(f'MRO:\t{C.__mro__}')
print('*'*106)


# ============= Changing the Parent Order =============
class A:
    def show(self):
        print('A')

class B:
    def show(self):
        print('B')

class C(B,A):
    pass

c = C()
c.show()
print(f'MRO:\t{C.__mro__}')
print('*'*106)


# ============= Using super() in MRO =============
''' super() follows the MRO, not just the immediate parent. '''
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")
        super().show()

class C(B):
    def show(self):
        print("C")
        super().show()

c = C()
c.show()
print(f'MRO:\t{C.__mro__}')
print('*'*106)


# ============= Diamond Problem =============
'''
    - Should Python visit A twice?      No.
    - Python uses the C3 Linearization Algorithm to create a consistent MRO.
'''
class A:
    def display(self):
        print("Class A")

class B(A):
    def display(self):
        print("Class B")
        super().display()

class C(A):
    def display(self):
        print("Class C")
        super().display()

class D(B, C):
    def display(self):
        print("Class D")
        super().display()

d = D()
d.display()
print(f'MRO:\t{D.__mro__}')
print('*'*106)