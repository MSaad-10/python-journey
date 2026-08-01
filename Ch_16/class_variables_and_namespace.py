'''
    - A class variable is a variable that belongs to the class itself, not to any individual object.
        * Only one copy of a class variable exists.
        * All objects of the class share that same copy.
'''


# ============= Example: Student Univerity Name =============
class Student:
    university = "UET Lahore"
    def __init__(self, name: str):
        self.name = name

s1 = Student('Saad')
print(s1.name)
print(Student.university)   # because university is class variable
print()
s2 = Student('Ali')
print(s2.name)
print(s2.university)        # same as above
print('*'*40)


# ============= Changing a Class Variable =============
class Student:
    university = "NUST"
    def __init__(self, name: str):
        self.name = name

Student.university = "FAST"     # changed to "FAST"
s1 = Student('Asad')
print(s1.name)
print(s1.university)
print()
s2 = Student('Aliyan')
print(s2.name)
print(Student.university)
print('*'*40)


# ============= What Happens If an Object Changes Class Variable? =============
class Student:
    university = "UET Lahore"
    def __init__(self, name: str):
        self.name = name

s1 = Student('Ahmar')
s1.university = "FAST"      # Python creates a new instance variable named university for s1.
print(s1.name) 
print(s1.university)
print(Student.university)   # class variable remains same 
print()
s2 = Student('Abubakar')
print(s2.name)
print(s2.university)
print('*'*40)


# ============= Counting Objects =============
class Student:
    total_students = 0
    def __init__(self, name: str):
        print('New Student Created!!')
        self.name = name
        Student.total_students +=1

s1 = Student('Hassan')
print(s1.name)
print()
s2 = Student('Kamran')
print(s2.name)
print()
print(f'Total Students:\t {Student.total_students}')
print('*'*40)


# ============= Example: Value of PI =============
class Circle:
    PI = 3.14
    def __init__(self, radius: float):
        self.radius = radius

    def calc_circumference(self) -> float:
        return 2*Circle.PI*self.radius

    def calc_area(self) -> float:
        return Circle.PI*(self.radius**2)

c1 = Circle(5.2)
print(f'Area:         \t{c1.calc_area()}')
print(f'Circumference:\t{c1.calc_circumference()}')
print()
c2 = Circle(6)
print(f'Area:         \t{c2.calc_area()}')
print(f'Circumference:\t{c2.calc_circumference()}')
print('*'*40)


# ============= Example: Laptop Discount =============
class Laptop:
    discount_percent = 10
    def __init__(self, brand: str, model: str, price: int):
        self.brand_name = brand
        self.model_name = model
        self.price = price

    def apply_discount(self):
        return self.price - (Laptop.discount_percent/100)*self.price

l1 = Laptop('Lenovo', 'ThinkPad', 200000)
print(l1.brand_name)
print(l1.model_name)
print(l1.price)
print(l1.apply_discount())
print()
l2 = Laptop('Apple', 'MacBook Air', 500000)
print(l2.brand_name)
print(l2.model_name)
print(l2.price)
print(l2.apply_discount())
print('*'*100)


# ============= Example: Laptop Discount (Applying different discount_percent for each Object) =============
class Laptop:
    discount_percent = 10
    def __init__(self, brand: str, model: str, price: int):
        self.brand_name = brand
        self.model_name = model
        self.price = price

    def apply_discount(self):
        return self.price - (self.discount_percent/100)*self.price      # change it to 'self' to apply object's instance

l1 = Laptop('Lenovo', 'ThinkPad', 200000)
l1.discount_percent = 20
print(l1.__dict__)          # Object property to display object's attributes
print(l1.apply_discount())
print()
l2 = Laptop('Apple', 'MacBook Air', 500000)
l2.discount_percent = 50    
print(l2.__dict__)
print(l2.apply_discount())
print('*'*100)