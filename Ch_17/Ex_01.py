"""
    - Define a function named 'divide' that takes two arguments.
    - Add exceptions for 0 and other data types such that:
        * divide(4,2)   ->   2.0
        * divide(4,0)   ->   Please do not divide by zero.
        * divide(4,'3') ->   Please enter inetegers only.      
"""


def divide(a: int, b: int):
    try:
        return a/b
    except ZeroDivisionError:
        print('Please do not divide by zero.')
    except TypeError:
        print('Please enter integers only.')           # can also print built in messages for errors


print(divide(4,2))
print(divide(4,0))
print(divide(4,'3'))