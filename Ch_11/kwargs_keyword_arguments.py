'''
    - **kwargs is used when you want a function to accept a variable number of keyword arguments.
    - While *args collects extra positional arguments into a tuple, **kwargs collects extra keyword arguments into a dictionary.
'''


# ===== What are Keyword Arguments? =====
    # A keyword argument is passed using 'name=value'
def student(name,age):
    print(f'Name:\t{name}')
    print(f'Age:\t{age}')

student(name='Saad', age=20)    # agruments & parameter names must match
print('\n')


# ===== Why Use **kwargs? =====
    # **kwargs are used when the function doesn't know what info a user might pass
def show(**kwargs):
    print(f'Output:\t{kwargs}')    # kwargs become dictionary
    print(f'Type:\t{type(kwargs)}')

show(Name='Saad', Age=20, City='Lahore')
print('\n')


# ===== Looping Through **kwargs =====
def display(**kwargs):
    for k,v in kwargs.items():
        print(k, '=', v)

display(Name='Saad', Age=20, City='Lahore')
print('\n')


# ===== kwargs is Just a Name =====
def elaborate(**info):
    return info         # returns 'Dictionary'

print(elaborate(name='lion', attribute='bravery'))
print('\n')


# ===== Combining Normal Parameters and **kwargs =====
def student(name,**kwargs):
    print(f'Name:   \t{name}')
    print(f'Details:\t{kwargs}')

student("Saad", age=20, city='Lahore')
print('\n')


# ===== Accessing Specific Values =====
def print_data(**kwargs):
    print(kwargs['name'])
    # print(kwargs['marks'])    #KeyError
    print(kwargs.get('marks'))

print_data(name="Saad", age=20, city='Lahore')
print('\n')


# ===== Using Both *args and **kwargs =====
def func(*args, **kwargs):
    print(f'Args:\t{args}')
    print(f'Kwargs:\t{kwargs}')

func(1,2,3,name='Saad',age=20)
print('\n')


# ===== Unpacking a Dictionary with ** =====
    # The ** operator can unpack dictionaries 
def student(name,age):    # parameter names must match key names
    print(name,age)

data = {
    'name': 'Saad',
    'age': 20
}
student(**data)
print('\n')


# ===== Order of Parameters =====       PADK (Parameters, *args, Default Parameters, **kwargs)
def parameters_order(a, b, *args, last_name = 'Ali', **kwargs):
    print(f'Parameters:        \t{a} {b}')
    print(f'*args:             \t{args}')
    print(f'Default Parameters:\t{last_name}')
    print(f'**kwargs:          \t{kwargs}')

parameters_order('A','B',1,2,3,'Cheema',name='Saad',age=20,city='Lahore')
print('\n')
parameters_order('A','B',1,2,3,name='Saad',age=20,city='Lahore')    
print('\n')


# # ===== Example =====
def create_user(**profile):
    for key, value in profile.items():
        print(f'{key}: {value}')
    
create_user(
    name = 'Saad',
    age = 20,
    country = 'Pakistan',
    field = 'Computer Science'
)