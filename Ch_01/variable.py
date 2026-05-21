''' ===== Data Type Definitions ===== '''

# String (str): Used for text data
name = "Saad"
print(name)

# Integer (int): Used for whole numbers
num = 12
print(num)

# Float (float): Used for decimal numbers 
gpa = 3.1
print(gpa)

# Boolean (bool): Logical flags
is_logged_in = True
is_valid = False

# Collections
numbers = [1, 2, 3]          # List list(): Mutable
print(numbers)
coordinates = (10, 20)       # Tuple tuple(): Immutable
print(coordinates)
unique_numbers = {1, 2, 3}   # Set set(): Unique values
print(unique_numbers)
student = {"name": "Saad", "age": 20}  # Dictionary dict(): Key-value pairs
print(student)

''' ===== Variable Initialization ===== '''
# Multiple assignment 
name, age = "Saad", 20
print("Name: " + name + "\n" + "Age: " + str(age))

# Chained assignment
x = y = z = 1
print(f"x: {x}\ny: {y}\nz: {z}")

''' 
    What is Dynamic Typing?
    - Python identifies the type at runtime based on the value assigned.
    - A variable can hold different data types throughout its lifecycle.
'''

name = 'Saad'
print(name)
name = 123
print(name)

''' ===== Variable Naming Rules ===== '''

#1. Must start with a letter or underscore _
name = "Saad"
_age = 20

#2. Cannot start with a number
# 2value = 10   ❌

#3. Only letters, digits, and underscores allowed
my_name = "Saad"
# my-name = "Saad"   ❌

#4. Case-sensitive
name = "Saad"
Name = "Ali"
print(name) 
print(Name)

#5. Cannot use Python keywords
# if = 10   ❌

''' ===== Variable Naming Conventions ===== '''

#1. Use meaningful names
# x = 10      ❌
age = 10  

#2. Use snake_case
student_name = "Saad"
total_marks = 90     

#3. Avoid single letters (except loops)
# a = 100       ❌
price = 100 
# for i in range(1,10): 

#4. Use uppercase for constants
PI = 3.14
MAX_LIMIT = 100