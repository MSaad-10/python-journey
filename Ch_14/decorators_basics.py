# '''
#     - A decorator is a function that takes another function as input, adds some extra behavior to it, and returns a new
#       function without changing the original function's code.
#     - A decorator "wraps" a function to add functionality before or after it runs.
# '''

# # ===== Core Concept =====
# def decorator_function(any_function):
#     def wrapper_function(text):
#         print(f'This is {text} function')
#         any_function()
#         print('Above is its execution')
#     return wrapper_function

# def func1():
#     print('This is function 1')

# def func2():
#     print('This is function 2')

# func1 = decorator_function(func1)
# func1('Awesome')
# print('\n')
# func2 = decorator_function(func2)
# func2('Bad')     


# # ===== Pythonic Syntax =====
# def decorator_function(any_function):       # decorator
#     def wrapper_function(text):
#         print(f'This is Awesome function')
#         any_function(text)
#         print('Above is its execution')
#     return wrapper_function

# @decorator_function
# def new_func(text):
#     print(f'This is {text} function')
# new_func('new')
# print('\n')

# @decorator_function
# def newest_func(text):
#     print(f'This is {text} function')
# newest_func('newest')


# # ===== Using *args and *kwargs =====
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print('BEFORE')
#         result = func(*args, **kwargs)
#         print('AFTER')
#         return result
#     return wrapper

# @decorator
# def add(a,b):
#     return a + b

# print(add(10,30))


# # ===== Example: Measuring Execution Time =====
# import time
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f'Execution Time: {end-start:.4f} seconds')
#         return result
#     return wrapper

# @timer
# def calculate():
#     total = sum(range(1000000))
#     return total

# total = calculate()
# print(total)


# ===== Use of wraps =====
from functools import wraps     # Test this code without using wraps
def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """ This is a wrapper function """
        print('This is Awesome Function')
        return func(*args, **kwargs)
    return wrapper

@decorator
def add(a,b):
    ''' Returns the sum of two numbers '''
    return a + b

print(add.__name__)
print(add.__doc__)