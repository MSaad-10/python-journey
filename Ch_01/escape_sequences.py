''' Escape sequences are used with backslash \ to give special meaning inside strings '''

# \' is used to include a single quote inside a string
print('hello \'ugly\' world')
print('I\'m Saad')

# \" is used to include a double quote inside a string
print("hello \"beautiful\" world")
print("He said \"Hello\"")

# \n is used to add a new line inside a string
print("Line A \nLine B \nLine C")

# \t is used to add a tab space inside a string
print("Name:\t Muhammad Saad")
print("Reg No:\t 2024-CS-665")

# \\ is used to print a single backslash inside a string
# print("This is backslash \")   ❌
print("This is backslash: \\")
print("This is double backslash: \\\\")

# \b is used add backspace i.e removes one character before it 
print("hel\bllo")

''' ===== Escape Sequences as Normal Text ===== '''

# Output: Line A \n Line B
print("Line A \\n Line B")

# Output: Line B \t line b
print("Line B \\t line b")

# Output: These are 4 backslashes: \\\\
print("These are 4 backslashes: \\\\\\\\")

# Output: \" \' 
print("\\\" \\\'")
