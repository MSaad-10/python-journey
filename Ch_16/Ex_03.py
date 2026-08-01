'''
    - Create a Person class that:
        * contains a counter class variable that keeps the record of number of objects of Person class.
'''


class Person:
    total_persons = 0
    def __init__(self, name: str, age: int):
        print('New Person Created!!')
        self.name = name
        self.age = age
        Person.total_persons += 1

p1 = Person('Saad', 18)
print(p1.__dict__)
print(f"Total instances created: {Person.total_persons}")