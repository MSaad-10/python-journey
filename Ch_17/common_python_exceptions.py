"""
    What is an Exception?
        - An exception is a problem that occurs while Python is executing your program.
    Compile-Time vs. Runtime Exceptions
        - Standard exceptions like ValueError, TypeError, or KeyError occur while the Python interpreter executes code (runtime).
        - However, SyntaxError and IndentationError are caught earlier during Python's parsing/compilation stage before any bytecode execution begins.    
"""


# ============= SyntaxError =============
''' Occurs when Python doesn't understand your code's syntax. '''
# def func:             # () missing
#     pass

# name = 'saad'*        # remove ';' 


# ============= IndentationError =============
''' Python uses indentation to define blocks. '''
# def func():
#         print('hello')
#     print('hii')        # tab needed


# ============= NameError =============
''' Occurs when you try to use a variable or name that hasn't been defined. '''
# print(first_name)       # define 'first_name' then print
# print(my_func)          # define 'my_func' first


# ============= TypeError =============
''' Occurs when you perform an operation using an inappropriate type. '''
# print(5 + 'hello')      # type of operands must be same
# len(10)                   # integer does not have length


# ============= IndexError =============
''' Occurs when you try to access an index that doesn't exist. '''
# l = [1,2,3]
# print(l[4])


# ============= ValueError =============
''' A ValueError occurs when the type is appropriate but the value is invalid. '''
# s = 'abc'
# print(int(s))

# num = int('hello')


# ============= AttributeError =============
''' Occurs when an object doesn't have the attribute or method you're trying to access. '''
# l = [1,2,3]
# l.push(123)


# ============= KeyError =============
''' Occurs when you try to access a dictionary key that doesn't exist. '''
# my_dict = {
#     'name': 'Saad'
# }
# print(my_dict['age'])


# ============= ZeroDivisionError =============
# print(10/0)
# print(10//0)
# print(10%0)


# ============= FileNotFoundError =============
''' Occurs when Python tries to open a file that doesn't exist. '''
# file = open('student.txt')


# ============= ModuleNotFoundError =============
''' Occurs when Python can't find the module you're trying to import. '''
# import sklearn      # not installed


# ============= ImportError =============
''' The module may exist, but the thing you're trying to import may not exist inside it. '''
# from math import algebra


# ============= RecursionError =============
''' Occurs when a recursive function calls itself too many times. '''
# def hello():
#     hello()

# hello()


# ============= AssertionError =============
''' Occurs when an assert statement evaluates to False. '''
# age = 12
# assert age >= 17