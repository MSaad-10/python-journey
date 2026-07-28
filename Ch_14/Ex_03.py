'''
    - Define a decorator that checks whether the passed list of arguments are all integers or not.
        * if all passed arguments are integers then return sum of integers.
        * if there exist an argument of data type other then integer then prints "Invalid arguments" message.
'''


from functools import wraps

# decorator
def only_int_allow(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if all(type(arg) is int for arg in (*args, *kwargs.values())):
            return func(*args, **kwargs)
        else:
            return "Invalid Arguments"
    return wrapper

@only_int_allow
def add(*args):
    return sum(args)

print(add(1,2,3,4,5))