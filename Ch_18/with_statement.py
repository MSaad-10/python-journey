"""
    - The 'with' statement automatically closes the file after the nested block of code. 
    - This is the preferred way to handle files in Python.
    - It ensures that the file is properly closed even if an error occurs.
"""


# ============= Basic Example =============
with open ('file.txt', 'r', encoding='utf-8') as file:
    data = file.read()
    print(data)
print()
print(f'Is the file closed? {file.closed}')
print('*'*40)   


# ============= Managing Multiple Files =============
''' Python allows you to manage multiple context managers in a single with statement. '''
with (
    open('file.txt', 'r', encoding='utf-8') as src,
    open('destination.txt', 'w', encoding='utf-8') as dest,
):
    dest.write(src.read())
print('*'*40)