''' 
    - String indexing means accessing individual characters of a string using their position (index).
'''

language = "Python"

#   P = 0, -6
#   y = 1, -5
#   t = 2, -4
#   h = 3, -3
#   o = 4, -2
#   n = 5, -1

# Access characters
print(language[0])
print(language[1])

# Negative Indexing
print(language[-1])  # last char
print(language[-3])

''' =========== Important Rules =========== '''

# Index out of range
# print(language[7])   ❌

# Strings are immutable
# language[0] = "p"   ❌

''' =========== Use Cases =========== '''

# Get first character
print(language[0])

# Get last character
print(language[-1])

# Loop through string
for ch in language:
    print(ch, end=" ")
