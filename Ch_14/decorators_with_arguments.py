from functools import wraps

# ===== Allowed Data Type =====
def only_data_type_allow(data_type):            # function to set the data type argument 
    def decorator(func):                        # original decorator function
        @wraps(func)
        def wrapper(*args, **kwargs):
            if all([type(arg)==data_type for arg in args]):
                return func(*args, **kwargs)
            else:
                return "Invalid Arguments"
        return wrapper
    return decorator

@only_data_type_allow(str)
def string_join(*args):
    return ''.join(args)

print(string_join('muhammad', ' ', 'saad'))
print()


# ===== Number of Repetitions =====
def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper():
            for _ in range(times):
                func()
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hello")

greet()
print()


# ===== Role Authorization =====
def require_role(role):
    def decorator(func):
        @wraps(func)
        def wrapper():
            print(f'Checking role: {role}')
            func()
        return wrapper
    return decorator

@require_role("User")
def dashboard():
    print("Dashboard Opened")

dashboard()
print()


# ===== Passing Arguments =====
def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(2)
def greet(name):
    print(f'Hello {name}')

greet('Saad')