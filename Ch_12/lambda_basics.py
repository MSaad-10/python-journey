'''
    - In Python, a lambda function is a small anonymous function defined using the lambda keyword.
    - It can take any number of arguments but can contain only a single expression.
'''


# ===== Square of Number =====
def square(x):
    return x**2
print(f'Simple:\t\t{square(5)}')
print(f'{square}')              # shows name of function

square_lambda = lambda a: a**2
print(f'Lambda:\t\t{square_lambda(6)}')
print(f'{square_lambda}')       # shows <lambda> means anonymous function
print('\n')


# ===== Sum of Numbers =====
def add(a,b):
    return a + b
print(f'Simple:\t\t{add(2,3)}')

add_lambda = lambda x,y: x+y
print(f'Lambda:\t\t{add_lambda(4,3)}')
print('\n')


# ===== Even Number Test =====
def is_even(num):
    if num%2 == 0:
        return True
    return False
print(f'Simple:\t\t{is_even(5)}')

is_even_lambda = lambda n: n%2==0   # Lambda Expression
print(f'Lambda:\t\t{is_even_lambda(6)}')
print('\n')


# ===== String Last Character =====
def last_char(l):
    return l[-1]
print(f'Simple:\t\t{last_char('Saad')}')

last_char_lambda = lambda s: s[-1]    # Lambda Expression
print(f'Lambda:\t\t{last_char_lambda('Ashfaq')}')
print('\n')


# # ===== String Length Tester =====
def str_len(s):
    if len(s) > 5:
        return True
    return False
print(f'Simple:\t\t{str_len('Saad')}')

str_len_lambda = lambda s: len(s) > 5 
print(f'Lambda:\t\t{str_len_lambda('jwijdow')}')
print('\n')


# ===== Using with map() =====
numbers = [1,2,3,4,5]
squares = list(map(lambda x: x**2, numbers))
print(f'Lambda:\t\t{squares}')

def squared(num):
    return num**2

squared = list(map(squared, numbers))
print(f'Simple:\t\t{squared}')