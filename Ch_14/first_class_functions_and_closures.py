'''
    First-Class Functions
        - In Python, functions are objects.
        - This means a function can do almost everything that other objects (like integers, strings, and lists) can do.
        - A function can:
            * Be assigned to a variable.
            * Be passed as an argument to another function.
            * Be returned from another function.
            * Be stored in lists, dictionaries, or other data structures.
        
'''


# ===== Example =====
def square(a):
    return a**2

s = square
print(s(3))

print(s.__name__)
print(square.__name__)

print(s)
print(square)
print('\n')


# ===== Assigning a Function to a Variable =====
def greet():
    print("Hello!")

say_hello = greet       # Stores the function object itself.
say_hello()
print('\n')


# ===== Passing a Function as an Argument =====
def greet():
    print("Good Morning!")

def execute(func):
    func()

execute(greet)
print('\n')


# ===== Returning a Function =====
def outer():
    def inner():
        print("Hello")
    return inner

result = outer()
result()
print('\n')


# ===== Functions in a List =====
def add():
    print("Addition")

def subtract():
    print("Subtraction")

operations = [add, subtract]
operations[0]()
operations[1]()
print('\n')


'''
    Clousres
        - A closure is a special kind of function.
        - A closure is an inner function that:
            * Is defined inside another function.
            * Uses variables from the outer function.
            * Continues to remember those variables even after the outer function has finished executing.
'''


# ===== Example =====
def outer():
    message = "Hello"
    def inner():
        print(message)
    return inner

greet = outer()
greet()
print('\n')


# ===== Function Factory =====
def multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = multiplier(2)
print(double(5))
print('\n')


# ===== Checking the Closure =====
def outer():
    x = 10
    def inner():
        print(x)
    return inner

f = outer()
print(f.__closure__)


# ===== Relationship with Closures =====
#   👉 Not a Closure because inner() doesn't use any variable from outer().
def outer():
    def inner():
        print('Hello')
    return inner

#   👉 A Closure because inner() uses message from outer().
def outside():
    message = "Hello"
    def inside():
        print(message)
    return inside