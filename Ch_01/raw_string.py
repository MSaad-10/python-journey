''' 
    - A raw string is a string in which Backslashes are treated as normal characters and escape sequences are ignored.
    - To create a raw string, letter 'r' is used as a string prefix, not as a function or keyword 
'''

# Raw String
print(r"Line A \n Line B")

''' =========== Use cases of 'r' =========== '''

# File Paths (Windows)
path = r"D:\python-journey\Ch_01"  

# Combined with f-strings
name = "Saad"
print(rf"Hello! \n {name}")

# Regular Expression (regex)
import re
pattern = r"\d+"    # without r, the compiler will read \d as an escape seq. which will create an ERROR
text = "I have 3 cats and 25 dogs"
result = re.findall(pattern,text)    # Pattern: "Match one or more consecutive digits."
print(result)       