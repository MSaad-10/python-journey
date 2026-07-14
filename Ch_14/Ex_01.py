'''
    - Define a decorator that:
        * modifies a function by adding the print statement.
        * prints the doc string of the function which is modified. 
        * returns the return value of the function.
    - Example:
        * Output should be like this:
            You  are calling add function
            {prints the docstring of function}
            {Return value of function}
'''


from functools import wraps
def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'You are calling {func.__name__} function')
        print(func.__doc__.strip() if func.__doc__ else "No docstring provided.")
        return func(*args, **kwargs)
    return wrapper

@decorator
def add(a,b):
    ''' This function takes two numbers as parameters and return their sum '''
    return a + b

print(add(10,30))