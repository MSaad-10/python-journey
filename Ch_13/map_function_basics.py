'''
    - In Python, map() is a built-in function used to apply a function to every item in an iterable (such as a list, tuple, or set).
    - map() can take multiple iterables if the function accepts multiple arguments.
    - Syntax:
                map(function, iterable)
'''


# ===== Square of Numbers =====
numbers = [1,2,3,4,5]
squared = list(map(lambda x:x**2, numbers))     # lambda function in map()
print(squared)
print('\n')


# ===== Converting Strings to Integers =====
strings = ['1','2','3','4','5']
integers = list(map(int,strings))
print(integers)
print('\n')


# ===== Using a Regular Function =====
def greet(name):
    return f"Hello {name}"

names = ['Alice', 'Bob', 'Max']
greetings = list(map(greet, names))
print(greetings)
print('\n')


# ===== Multiple Iterables =====
num1 = [1,2,3]
num2 = [4,5,6]
print(list(map(lambda a,b: a+b, num1, num2)))
print('\n')


# ===== Iterating map() Function =====
currencies = ['dollar', 'yuan', 'riyal']
currency = map(len, currencies)
for i in currency:
    print(i, end='   ')
# following loop will not work
for j in currency:        # iterables [map() function] can be iterated only once
    print(j)