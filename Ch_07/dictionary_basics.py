'''
    - Dictionary is a data structure in Python that stores data in "key : value" pair.
    - Dictionaries are mutable.
'''


# ===== Simple Example =====
student = {
    "name": "Saad",
    "age": 20,
    "city": "Lahore"
}
print(f'Student:  \t  {student}')
person = dict(name = 'Ali', age = 25)
print(f'Person:     \t  {person}')
print('\n')


# ===== Adding Items =====
# Use keys instead of indexes
student = {
    "name": "Saad",
    "age": 20
}
print(f"student['name']:  {student["name"]}")
print('\n')


# ===== Adding new key-value pair =====
student['gpa'] = 3.58
print(f'Original:\t{student}')
student['city'] = 'Lahore'
# Update existing key-value pair
student['age'] = 21
print(f'Updated:\t{student}')
print('\n')


# ===== Nested Dictionaries =====
student = {
    'name': 'Saad',
    'age': 20,
    'marks': {
        'maths': 100,
        'cs':  95
    }
}
print(f'Name:\t{student.get('name')}')
print(student.get('city'))   # returns 'None' 
print(f'Maths:\t{student['marks']['maths']}')
print('\n')


# ===== Dictionary Membership =====
# checks keys only
marks = {
    'ali': 78,
    'saad': 100,
    'asad': 71
}
print('ali' in marks)
print(71 in marks)   # always returns False
# to check values
print(100 in marks.values())
print('\n')


# ===== Duplicate key in dict =====
user = {
    'name' :'Saad', 
    'height' : 5.7, 
    'height' : 5.8   
}   # the later value will be overwritten
print(f'User:\t{user}')