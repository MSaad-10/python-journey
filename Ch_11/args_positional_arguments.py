'''
    - *args is used in Python functions when you want to accept a variable number of positional arguments.
    - Normally, a function expects a fixed number of arguments:
            def add(a, b):
                return a + b
            print(add(10, 20))
            print(add(10, 20, 30))   # TypeError
      because the function expects only 2 arguments.
'''


# ===== Using *args =====
def add(*args):
    print(args)

add(10,20,30,40)    # returns 'Tuple'
print('\n')


# ===== How *args Works? =====
def show(*args):
    print(f'Output:\t{args}')
    print(f'Type:\t{type(args)}')

show(1,2,3,4,5)
print('\n')


# ===== Looping Through *args =====
def display(*args):
    for item in args:
        print(item, end=" ")
    print('\n')

display('Saad', 'Ali', 'Hamza')


# ===== Sum of Numbers =====
def sum(*nums):    # args is just a name
    total = 0
    for i in nums:
        total += i
    return total

print(f'Sum1:\t{sum(1,2,3,4)}')
print(f'Sum2:\t{sum(5,6)}')
print(f'Sum3:\t{sum(5)}')
print('\n')


# ===== Mixing Normal Parameters and *args =====
def student(name, *marks):
    print(f'Name:\t{name}')
    print(f'Marks:\t{marks}')

student('Saad',10,20,30,40)

def teacher(*args, name):    
    print(f'Name:\t{name}')
    print(f'Marks:\t{args}')

teacher(21,34,12,12)    # TyeError: arguments passed positionally
teacher(21,34,12,12, name = "Saad")    # Works fine as arguments are passed explicitly with naming keyword
print('\n')


# ===== Unpacking with * =====
numbers = [10,20,30,40]
print('With *:\t    ', *numbers)
print('Without *:  ', numbers)
print('\n')


# ===== Using *args With Other Parameters =====
def info(a,b,*args):
    print(f'A:   \t{a}')
    print(f'B:   \t{b}')
    print(f'args:\t{args}')
    
info(1,2,3,4,5,6)
print('\n')


# ===== *args as Function Argurment =====
def multiply_nums(*args):
    product = 1 
    for i in args:
        product *= i
    return product

numbers = [2,3,4]
print(f'Product:\t{multiply_nums(*numbers)}')    # List unpacking
nums = (5,6,3,4)
print(f'Product:\t{multiply_nums(*nums)}')    # Tuple unpacking