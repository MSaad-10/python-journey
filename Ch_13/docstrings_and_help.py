'''
    DOC STRING
            - A docstring (documentation string) is a string literal placed as the first statement inside a module, function, class, or method. 
            - It describes what that code does.
            - Unlike comments (#), docstrings are stored by Python and can be accessed later.
            - Doc Strings can contain multiple lines.
            - Syntax:
                        def function_name():
                            """Documentation goes here."""   OR  it can also be written in triple single quotes
    help() FUNCTION
            - The help() function displays documentation about Python objects.
            - It can show:
                * Functions
                * Classes
                * Modules
                * Built-in functions
                * Your own functions
            - It displays:
                * Function name
                * Parameters
                * Docstring
'''


# ===== Basic Example =====
def add(a,b):
    ''' Returns the sum of two numbers '''
    return a+b
print(add.__doc__, '\n')
print(help(add))
print('\n')


# ===== For Built-in Functions =====
print(len.__doc__, '\n')
print(help(len))
print('\n')


# ===== Docstrings for Classes =====
class Student:
    ''' Represents a student with name and marks. '''
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

print(help(Student))
print(Student.__doc__)
print('\n')


# ===== Docstrings for Methods =====
class Calculator:
    def multiply(a,b):
        ''' Multiplies two numbers. '''
        return a*b

print(Calculator.multiply.__doc__)
print('\n', help(Calculator.multiply))