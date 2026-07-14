# ===== Returning a Function Object =====
def outer_func():
    def inner_func():
        print('Inside Inner Function')
    return inner_func            # Return the function itself, not its result.

message = outer_func()
message()


# ===== Calling the Inner Function Immediately =====
def outer():
    def inner():
        print('control inside inner')  
    return inner()          # Executes the function first then returns whatever it returns

outer()


# ===== Creating a Closure with a Captured Value =====
def outside(msg: str):
    def inside():
        print(f'Message is {msg}')
    return inside

result = outside("hello world!")
result()


# ===== Practical Example =====
def power(exponent):
    def calculate(number):
        return number ** exponent
    return calculate

square = power(2)
cube = power(3)
print(f'Square of 5:\t{square(5)}')
print(f'Cube of 3:  \t{cube(3)}')