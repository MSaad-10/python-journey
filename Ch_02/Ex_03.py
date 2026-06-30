'''
    Take two comma separated inputs from user:
        1. User's name
        2. A single character
    Output two following things:
        1. User's name length
        2. Count the character that user inputed (bonus: case insensitive count)
'''

name, char = input("Enter your name and a character (comma separated): ").split(',')
print(f"Length: {len(name.strip().replace(" ",""))}")

# 1. case insensitive search
if (char>='A')&(char<='Z'):
    name = name.upper()
else:
    name = name.lower()
print(f"Count: {name.count(char)}")

# 2. case insensitive search
print(f"Count: {name.lower().count(char.lower())}")
print(f"Count: {name.lower().strip().count(char.lower().strip())}")   # optimal