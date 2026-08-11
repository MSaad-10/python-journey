"""
    File Data Descriptors in Python
        - There are two most used data descriptors in Python for file objects:
            * .name → Returns the name of the file.
            * .closed → Returns True if the file is closed, otherwise it returns False.
"""

# ============= file.name =============
file = open('file.txt', 'r', encoding='utf-8')
print(f'File name: {file.name}')
file.close()
print('*'*40)


# ============= file.closed =============
''' The closed attribute returns True if the file is closed, otherwise it returns False. '''
file = open('file.txt', 'r', encoding='utf-8')
print(f'Is the file closed? {file.closed}')
file.close()
print(f'Is the file closed? {file.closed}')
print('*'*40)


# ============= file.mode =============
''' The mode attribute returns the mode in which the file was opened. '''
file = open('file.txt', 'r', encoding='utf-8')
print(f'File mode: {file.mode}')
file.close()
print('*'*40)


# ============= file.encoding =============
''' The encoding attribute returns the encoding used to decode or encode the file. '''
file = open('file.txt', 'r', encoding='utf-8')
print(f'File encoding: {file.encoding}')
file.close()
print('*'*40)


# ============= file.newlines =============
''' The newlines attribute returns the type of newlines encountered in the file. '''
file = open('file.txt', 'r', encoding='utf-8')
print(f'File newlines: {file.newlines}')
file.close()
print('*'*40)


# ============= Complete Attribute Inspection Example =============
with open('file.txt', 'r', encoding='utf-8') as file:
    print(f"Name:     {file.name}")      
    print(f"Mode:     {file.mode}")      
    print(f"Encoding: {file.encoding}")  
    print(f"Closed:   {file.closed}")    
print(f"Closed:   {file.closed}")        
print(f"Newlines: {file.newlines}")
print('*'*40)