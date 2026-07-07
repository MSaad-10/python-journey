'''
    - List comprehension is a compact way to create lists using loops and conditions.
    - It allows you to create lists in a short and clean way using a single line of code.
'''


# ===== List of Square from 1 to 10 =====
squares = []
for i in range(1,11):
    squares.append(i**2)
print(f'Simple:\t\t{squares}')

squares_comp = [i**2 for i in range(1,11)]
print(f'Comprehension:\t{squares_comp}')
print('\n')


# ===== List of Negatives from 1 to 10 =====
negative = []
for i in range(1,11):
    negative.append(-i)
print(f'Simple:\t\t{negative}')

negative_comp = [-i for i in range(1,11)]
print(f'Comprehension:\t{negative_comp}')
print('\n')


# ===== List Containing Names Initials =====
names = ['Saad', 'Ali', 'Hassan']
initials = []
for name in names:
    initials.append(name[0])
print(f'Simple:\t\t{initials}')

initials_comp = [name[0] for name in names]
print(f'Comprehension:\t{initials_comp}')
print('\n')


# ===== List of Even Numbers from 1 to 10 =====
evens  = []
for i in range(1,11):
    if i%2 == 0:
        evens.append(i)
print(f'Simple:\t\t{evens}')

evens_comp = [i for i in range(1,11) if i%2 == 0]   # if-condition in comprehension
print(f'Comprehension:\t{evens_comp}')
print('\n')


# ===== Converting Strings to Uppercase =====
names = ['ali', 'saad', 'hassan']
upper = []
for name in names:
    upper.append(name.upper())
print(f'Simple:\t\t{upper}')

upper_comp = [name.upper() for name in names]
print(f'Comprehension:\t{upper_comp}')
print('\n')


# ===== Differentiating Even & Odd Numbers =====
nums = list(range(1,11))
even_odd = []
for i in nums:
    if i%2 == 0:
        even_odd.append(f'{i}-Even')
    else:
        even_odd.append(f'{i}-Odd')
print(f'Simple:\t\t{even_odd}')

even_odd_comp = [f'{i}-Even' if i%2==0 else f'{i}-Odd' for i in nums]   # if-else condition in comprehension
print(f'Comprehension:\t{even_odd_comp}')
print('\n')


# ===== Nested List Comprehension =====
matrix = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(i*j)
    matrix.append(row)
print(f'Simple:\t\t{matrix}')

matrix_comp = [[i*j for j in range(3)] for i in range(3)]
print(f'Comprehension:\t{matrix_comp}')
print('\n')


# ===== Creating List from String =====
lang = 'Python'
chars = []
for ch in lang:
    chars.append(ch)
print(f'Simple:\t\t{chars}')

chars_comp = [ch for ch in lang]
print(f'Comprehension:\t{chars_comp}')