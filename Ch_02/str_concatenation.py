'''  
    - String concatenation means Joining two or more strings together 
'''

''' =========== Ways of Concatenation =========== '''

# Using + Operator
a = 'Hello'
b = 'World'
print(a + " " + b)

# Using , in print()
print("Hello","World")   # automatically adds space

# Using f-strings
name = 'Saad'
age = 20
print(f"My name is {name} and I am {age} years old")

# Using .join()
words = ["Hello", "World"]
print(" ".join(words))   # " " is printed b/w each item of words

name = "Saad"
print(" ".join(name))   # " " is joined with each character of name

# Using +=
text = "Hello"
text += " "
text += "World"
print(text)

''' =========== Use Cases =========== '''

# Creating Messages
name = "Saad"
print("Hello " + name)

# Building File Paths
folder = 'Documents'
file = 'test.txt'
path = folder + "/" + file
print(path)

# Combining User Input
first = input("First name: ")
last = input("Last name: ")
print(first + " " + last)

# Loop-Based String Building
result = ""
for i in range(3):
    result += "Hi "
print(result)

# Formatting Output
name = 'Saad'
marks = 90
print("Name: " + name + "\n" + "Marks: " + str(marks))

''' =========== Important Scenarios =========== '''

# Cannot concatenate different types directly
age = 20
# print("Age is " + age)   ❌
print("Age is " + str(age))

# Performance Issue
text = ""
for i in range(1000):   # slow for large data
    text += "a"
print(text)

print("".join(["a"])*1000) # ✅ fast

# Missing Spaces
print("Hello" + "World")
print("Hello" + " " + "World")  # must add space manually
print("Hello","World")  # or use this for automatically adding space
