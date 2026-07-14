'''
    - Define a decorator that:
        * calculates the time taken by a fucntion to execute completely.
'''


import time
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f'Execution Time: {end-start:.4f} seconds')
        return result
    return wrapper

@decorator
def time_func(x):
    return [i**2 for i in range(1, x+1)]

time_func(1000)