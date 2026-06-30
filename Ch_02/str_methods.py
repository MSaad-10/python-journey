''' 
    - String methods are the built-in functions that perform operations on strings.
    - Strings are Immutable so methods do NOT change original string.
'''

name = "mUhAmMaD sAaD"

''' =========== Important Methods =========== '''

# upper() --- converts string to uppercase
print(f"Upper: {name.upper()}")

# lower() --- converts string to lowercase
print(f"Lower: {name.lower()}")

# title() --- capitalizes first letter of each word
print(f"Title: {name.title()}")

# capitalize() --- capitalizes first letter only
print(f"Capitalize: {name.capitalize()}")

# strip() --- removes spaces from both sides
text = "     SAAD     "
dots = ".............."
print(f"Plain: {text + dots}")
print(f"LStrip: {text.lstrip() + dots}")    # removes characters from left side
print(f"RStrip: {text.rstrip() + dots}")    # removes characters from right side
print(f"Strip: {text.strip() + dots}")      # removes characters from both sides

# replace() --- replaces text
    # Syntax: str.replace(old, new, count)
text = "I like Java"
print(text.replace("Java", "Python"))
print(text.replace(" ", "_", 1))   # replaces only first space
print("She is beautiful and she is good dancer".replace("is","was",100))   # replaces all 'is' with 'was' 

# find() --- finds index of character/word
    # Syntax:  str.find(text, start_index, end_index)   --- returns -1 in case character/word not found
text = "the Python"
print(text.find("t"))
print(text.find("t",2,5)) # search from 'e' to 'y'
print(text.find("t",3))   # search from ' '

# count() --- counts occurrences
text = "banana"
print(text.count("a"))

# startswith() --- checks beginning
text = "Python"
print(text.startswith("Py"))

# endswith() -- checks ending
word = "Nodejs"
print(word.endswith("on"))

# split() --- splits string into list
text = "apple banana mango"
print(text.split())

# join() --- joins elements into string
words = ["Hi", "Saad"]
print(" ".join(words))
print("-".join(words))

# center() --- aligns str in center by adding padding on both sides
    # Syntax: str.center(width, fillchar)
text = "Saad"
print(text.center(12,'*'))
print(text.center(5,'^'))   # '^' will be added on left side


''' =========== Checking Methods =========== '''

# isaplha() --- only letters?
print("Hello".isalpha())

# isdigit() -- only numbers? 
print("a123".isdigit())

# isalnum() -- letters + numbers?
print("abc123".isalnum())

# Methods do not change the original string
name = "saad"
print(name.upper())
print(name)
