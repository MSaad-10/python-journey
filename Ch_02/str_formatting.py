''' 
    - String formatting means inserting variables or values inside a string in a clean and readable way.
'''

name = 'Saad'
age = 20

# Using + (concatenation)
print("hello " + name + " your age is " + str(age))

# Using .format() method 
print("hello {} your age is {}".format(name,age))   # used in python3
 
# Using , in print()
print("hello",name,"your age is",age) 

# Using f-strings
print(f"hello {name} your age is {age}")

''' =========== Advanced f-string Examples =========== '''

# Expressions inside f-strings
a = 10
b = 5
print(f"Sum is {a + b}")

# Formatting numbers
PI = 3.14159
print(f"Value of PI: {PI:.2f}") 

# Aligning text
    # Syntax: {value:fill_alignwidth}
name = "Saad"
print(f"{name:.>10}")   # > right align
print(f"{name:*<10}")   # < left align
print(f"{name:-^10}")   # - center align


''' =========== Use Cases =========== '''

# Displaying user info
name = input("Enter name: ")
print(f"Hello, {name}")

# Mathematical Calculations
a = 5
b = 3
print(f"{a} + {b} = {a + b}")

# Showing results
marks = 85
print(f"Marks obtained: {marks}")