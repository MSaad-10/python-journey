'''
    - Following methods are used to remove data from a dictionary:
        1. .pop()
        2. .popitem()
        3. .clear()
        4. del operator
'''


# ===== .pop() =====
student = {
    "name": "Saad",
    "age": 20,
    "gpa": 3.78,
    "city": 'Lahore'
}
print(f'Student:\t{student}') 
popped_value = student.pop("gpa")
print(f'pop("gpa"):\t{popped_value}\nType:\t\t{type(popped_value)}')
print(f'Updated:\t{student}')
print('\n')


# ===== del Operator =====
print(f'Original:  \t{student}')
del student["city"]
print(f'del["city"]:\t{student}')
print('\n')


# ===== .clear() =====
student.clear()
print(student)
print('\n')


# ===== .popitem() =====
# removes last inserted item
student['religion'] = 'Islam'
print(f'Original:\t{student}')
popped_item = student.popitem()
print(f'popitem():\t{popped_item}\nType:\t\t{type(popped_item)}')
print(f'Updated:\t{student}')