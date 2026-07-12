# ===== Print the longest name =====
def func(item):
    return len(item)
names = ['saad', 'ali', 'umair']
simple_result = max(names, key = func)    # find max according to func
# simple_result = max(names, key = len)   # OR
print(f'Simple:       \t{simple_result}')

lambda_result = max(names, key = lambda item:len(item))
print(f'Comprehension:\t{lambda_result}')
print('\n')


# ===== Dictionaries inside List =====
students = [
    {'name': 'Saad', 'age': 18, 'score': 78},
    {'name': 'Asad', 'age': 20, 'score': 67},
    {'name': 'Ali', 'age': 19, 'score': 89},
]
print(f'Highest Score:\t{max(students, key = lambda item:item.get('score'))['name']}')
print(f'Highest Age:  \t{max(students, key = lambda item:item.get('age')).get('name')}')
print('\n')


# ===== Nested Dictionary Structure =====
student = {
    'Saad': {'score': 90, 'age': 24},
    'Ali': {'score': 75, 'age': 19},
    'Kamran': {'score': 85, 'age': 32}
}
print(f'Highest Score:\t{max(student, key = lambda element: student[element]['score'])}')
print(f'Highest Age:\t{max(student, key = lambda element: student[element]['age'])}')


'''
    - Same implementation goes for min() function.
'''