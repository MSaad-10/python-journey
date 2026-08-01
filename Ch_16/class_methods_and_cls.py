'''
    - A class method is a method that works with the class itself, not with individual objects.
    - Instead of receiving the current object (self), it receives the class as its first argument, conventionally named cls.
    - To define a class method, use the @classmethod decorator.
    - Class methods cannot use instance variables.
'''


# ============= Example: Counting number of class objects =============
class Person:
    total_persons = 0
    def __init__(self, name: str, age: int):
        print('New Person Created!!')
        self.name = name
        self.age = age
        Person.total_persons += 1

    @classmethod
    def count_instances(cls) -> str:
        return f"You have created {cls.total_persons} instances of {cls.__name__} class"

    def is_adult(self) -> bool:
        return self.age>=18

p1 = Person('Saad', 21)
print(p1.__dict__)
print(p1.is_adult())
print()
p2 = Person('Ali', 12)
print(p2.__dict__)
print(p2.is_adult())
print()
print(Person.count_instances())
print('*'*45)


# ============= Example: Changing University Name =============
class Student:
    university = "UET Lahore"
    def __init__(self, name: str):
        self.name = name 

    @classmethod
    def change_university(cls, name: str):
        cls.university = name

student1 = Student('Saad')
print(student1.__dict__)
print(student1.university)
Student.change_university("FAST")
print()
print(student1.university)
print('*'*40)


# ============= Alternative Constructors (Factories) =============
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @classmethod                    
    def from_string(cls, data_str: str) -> Person:      # Alternative constructor
        # Parse "Saad-21" into a new Person object
        name, age = data_str.split('-')
        return cls(name, int(age))

p1 = Person.from_string("Saad-21")
print(p1.__dict__)
print('*'*40)