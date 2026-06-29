''' 
    Regex (Regular Expression) is a pattern used to search, match, or extract text. 
    Regex helps to:
        ✔ Find specific patterns in text
        ✔ Extract useful data
        ✔ Validate input (emails, phone numbers, etc.)
        ✔ Clean messy data
'''

import re

# Find Numbers
text = "Room 101, Floor 2"
pattern = r"\d+"    # Pattern: "Match one or more consecutive digits."
result = re.findall(pattern, text)
print(result)

# Find Words
text = "Hello World"
print(re.findall("\\w+",text))

# Find Spaces
print(re.findall(r"\s","One Line Code"))



# Regex is made of symbols with meanings: 
#        Pattern             Meaning
#        -------             --------
#        \d                  digit(0-9)
#        \w                  word/letters 
#        \s                  space
#        +                   one or more
#        .                   any character