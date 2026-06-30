''' 
    - The input() function is used to take input (data) from the user through the keyboard.
    - input() always returns data as a string (str)
'''

# Basic Example
name = input("Enter your name: ")
print(f"Hello {name}")
age = int(input("Enter your age: "))
print(f"Your age is {age}")

''' =========== Converting input() to other types =========== '''

# Convert to integer
age = int(input("Enter your age: "))
print(f"You are {age} years old")

# Convert to float
gpa = float(input("Enter your gpa: "))
print(f"Your gpa is {gpa}")

''' =========== Use Cases =========== '''

# Taking User's Name
name = input("Enter your name: ")
print(f"Hello {name}")

# Taking Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a + b)

# Simple Calculator
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
print("Sum =", num1 + num2)

# Taking multiple inputs in single line
name, age = input("Enter your name and age: ").split()  # separated by space " "
print(name, age)

f_name, l_name = input("Enter your first & last name: ").split(",")   # separated by comma ","
print(f_name, l_name)