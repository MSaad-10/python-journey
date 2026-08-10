"""
    Exception Handling in Python
        - Exception handling allows your program to detect, catch, and handle runtime errors without crashing unexpectedly.
        - It is implemented using try and except block.
        - The 'try' block contains the code that might cause an exception.
        - 'except' tells Python what to do if a particular exception occurs.
            * Instead of the program crashing, Python executes the except block.

"""


# ============= Basic try/except =============
try:
    number = int(input('Enter a number: '))
    result = 10/number
    print(result)
except ZeroDivisionError:
    print("You can't divide by zero")
except:
    print('Invalid Input!')
print('*'*40)


# ============= Handling Multiple Exceptions =============
''' You can have multiple except blocks. '''
try:
    number = int(input('Enter a number: '))
    result = 100/number
    print(result)
except ValueError:
    print('Please enter a valid number')
except ZeroDivisionError:
    print('Number cannot be zero')
print('*'*40)


# ============= Catching Multiple Exceptions Together =============
try:
    number = int(input('Enter number: '))
    result = 100/number
    print(result)
except (ValueError, ZeroDivisionError):
    print('Invalid Input!')
except:
    print('Invalid Input!')
print('*'*40)


# ============= Using 'as' to Get the Error =============
''' You can store the exception object in a variable. '''
try:
    number = int('hello')
    print(number)
except ValueError as error:
    print(error)
    print(type(error))
print('*'*40)


# ============= else block =============
''' The else block executes only if no exception occurs. '''
try:
    number = int(input('Enter number: '))
    result = 100/number
except ValueError:
    print("Invalid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Calculation successful.")
    print(result)
print('*'*40)


# ============= finally =============
''' finally executes whether an exception occurs or not. '''
try:
    number = int(input('Enter a number: '))
    result = 10/number    
    print(result)
except ZeroDivisionError:
    print('Cannot divide by zero.')
except:
    print('Invalid Input')
finally:
    print('This will always excute.')


# ============= Why Do We Need finally? =============
''' It's commonly used for cleanup operations. '''
file = open('file.txt')
try:
    data = file.read()
    print(data)
finally:
    file.close()
print('*'*40)


# ============= Catching Exception =============
try:
    number = 10/0
except Exception as error:
    print(f'Something went wrong: {error}')
print('*'*40)


# ============= raise + Exception Handling =============
def set_age(age):
    if age<0:
        raise ValueError('Age cannot be negative')
    return age

try:
    age = set_age(-5)
except ValueError as error:
    print(f'Error: {error}')
print('*'*40)


# ============= Exception Propagation =============
''' An exception can travel up through function calls until something handles it. '''
def divide():
    return 10/0

def calculate():
    return divide()

try:
    calculate()
except ZeroDivisionError:
    print('Division by zero!')
print('*'*40)


# ============= Complete try-except-else-finally =============
try:
    number = int(input('Enter number: '))
    result = 100/number
except ValueError:
    print('Invalid Input!')
except ZeroDivisionError:
    print('Cannot divide by zero')
else:
    print(f'Result: {result}')
finally:
    print('Program Finished!')
print('*'*40)


# ============= Example =============
while True:
    try:
        age = int(input('Enter your age: '))
    except ValueError:
        print('Please enter integer!')
    except: 
        print('Unexpected error!')
    else:
        print(f'User Input: {age}')
        break
    finally:
        print("'finally' block executed")
    
if age>18:
    print('You can play this game')
else:
    print("You can't play this game")
print('*'*40)


# ============= Real-World Example =============
def process_file(file_path):
    try:
        file = open(file_path, "rb")
        data = file.read()
    except FileNotFoundError:
        print("TXT file was not found.")
    except PermissionError:
        print("You don't have permission to access this file.")
    else:
        print("File processed successfully.")
    finally:
        try:
            file.close()
        except UnboundLocalError:
            pass

process_file('file.txt')
process_file('new.txt')
print('*'*40)