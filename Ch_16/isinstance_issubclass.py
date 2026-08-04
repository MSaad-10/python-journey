"""
    What is isinstance()?
        - isinstance() checks whether an object belongs to a particular class.
        - It returns:   
            * True
            * False
        - Syntax:       isinstance(object, ClassName)
"""


# ============= Example 1 =============
class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()
print(isinstance(dog, Dog))     # Because dog is an object of the Dog class.
print(isinstance(dog, Animal))  # Because Dog inherits from Animal, so every Dog object is also an Animal.
print('*'*40)


# ============= Example 2 (Inheritance) =============
class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()
print(isinstance(dog, Cat))     # No relation between Dog and Cat class
print('*'*40)


# ============= Checking Multiple Classes =============
''' Python checks whether the object belongs to any class in the tuple. '''
class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()
print(isinstance(dog, (Dog, Animal)))
print('*'*40)


# ============= Built-in Types =============
''' isinstance() isn't limited to your own classes. '''
print(isinstance(10, int))
print(isinstance('Hello', str))
print(isinstance([1,2,3], list))
print(isinstance(True, bool))
print(isinstance(('a', 'b'), tuple))
print(issubclass(bool, int))        # bool class is actually a direct subclass of int.
print(isinstance(True, int))
print('*'*40)


"""
    What is issuclass()?
        - issubclass() checks whether one class inherits from another class.
        - It does not work with objects.
        - It returns:
            * True 
            * False
        - Syntax:       issubclass(ChildClass, ParentClass)
"""


# ============= Example 1 =============
class Animal:
    pass

class Dog(Animal):
    pass

print(issubclass(Dog, Animal))
print(issubclass(Animal, Dog))
print('*'*40)


# ============= Example 2 =============
class Animal:
    pass

class Dog(Animal):
    pass

class Labrador(Dog):
    pass

print(issubclass(Labrador, Animal))
print('*'*40)


# ============= Checking Multiple Parent Classes =============
''' Like isinstance(), issubclass() also accepts a tuple. '''
class Animal:
    pass

class Mammal:
    pass

class Dog(Animal):
    pass

print(issubclass(Dog, (Animal, Mammal)))    # Python performs logical OR evaluation.
print('*'*40)


# ============= Complete Example =============
''' isinstance() checks the object and issubclass() checks the class. '''
class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()
print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
print(issubclass(Dog, Animal))
print(issubclass(Animal, Dog))
print('*'*40)


# ============= Reflexivity and the Root Class =============
class Vehicle:
    pass

class Car(Vehicle):
    pass

car = Car()
print(issubclass(Car, Car))     # A class is always considered a subclass of itself.
print(issubclass(Vehicle, object))  # Every user-defined class ultimately inherits from Python's base object.
print(isinstance(dog, object)) 
print('*'*40)