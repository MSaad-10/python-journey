# String (str)
name = "Saad"
print(name)

# Integer (int)
num = 12
print(num)

# Floating Point (float)
gpa = 3.1
print(gpa)

# Boolean (bool)
is_logged_in = True
is_valid = False

# List (list)
numbers = [1, 2, 3]
names = ["Ali", "Saad"]

# Tuple (tuple)
coordinates = (10, 20)

# Set (set)
unique_numbers = {1,2,3}

# Dictionary (dict)
student = {
    "name": "Saad",
    "age": 20
}

# Variables declaration & initialization
name, age = "Saad", 20
print("Name: " + name + "\n" + "Age: " + str(age))

x = y = z = 1
print(f"x: {x}\ny: {y}\nz: {z}")

''' 
    =========== What is Dynamic Typing? ===========
    In Python:
        You don't declare a data type
        The type is decided automatically
        A variable can change its type during execution
'''

name = 'Saad'
print(name)
name = 123
print(name)

''' =========== Variable Naming Rules =========== '''

# Must start with a letter or underscore _
name = "Saad"
_age = 20

# Cannot start with a number
# 2value = 10   ❌

# Only letters, digits, and underscores allowed
my_name = "Saad"
# my-name = "Saad"   ❌

# Case-sensitive
name = "Saad"
Name = "Ali"
print(name) 
print(Name)

# Cannot use Python keywords
# if = 10   ❌


''' =========== Variable Naming Conventions =========== '''

# Use meaningful names
# x = 10      ❌
age = 10  

# Use snake_case
student_name = "Saad"
total_marks = 90     

# Avoid single letters (except loops)
# a = 100       ❌
price = 100 
# for i in range(1,10): 

# Use uppercase for constants
PI = 3.14
MAX_LIMIT = 100