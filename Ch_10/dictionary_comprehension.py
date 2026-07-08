'''
    - Dictionary comprehension is a short way to create dictionaries using loops and conditions.
    - It is similar to list comprehension, but it creates key-value pairs.
'''


# ===== Squared values =====
square_dict = {}
for i in range(1,11):
    square_dict[i] = i**2
print(f'Simple:\t\t{square_dict}')

print('Comprehension:')
square_nums = {f"Square of {nums} is":nums**2 for nums in range(1,11)}   # Using String as Key
for k,v in square_nums.items():
    print(f'{k} : {v}')
print('\n')


# ===== Counting Number of Characters in a String =====
name = "Muhammad Saad"
count_char = {char:name.count(char) for char in name}
print(f'Comprehension:\t{count_char}')

counter = {}
temp_var = ""
for char in name:
    if char not in temp_var:
        counter[char] = name.count(char)
        temp_var += char
print(f'Simple:\t\t{counter}')
print('\n')


# ===== Odd Even Illustration =====
odd_even = {i: f'Even' if i%2==0 else f'Odd' for i in range(1,11)}   # if-else in dict_comprehension
odd_even = {i: ('Even' if i%2==0 else 'Odd') for i in range(1,11)}   # Alternative
print(f'Comprehension:\t{odd_even}')

nums = {}
for i in range(1,11):
    if i%2==0:
        nums[i] = 'Even'
    else:
        nums[i] = 'Odd'
print(f'Simple:\t\t{nums}')
print('\n')


# ===== Even Squares Only =====
evens = {i:i**2 for i in range(1,11) if i%2==0}   # if in dict_comprehension
print(f'Comprehension:\t{evens}')

even_nums = {}
for i in range(1,11):
    if i%2==0:
        even_nums[i] = i**2
print(f'Simple:\t\t{even_nums}')
print('\n')


# ===== Creating Dictionary from List =====
names = ['Ali', 'Saad', 'Ahmad', 'Aliyan']
names_length = {name:len(name) for name in names}
print(f'Comprehension:\t{names_length}')

d = {}
for name in names:
    d[name] = len(name)
print(f'Simple:\t\t{d}')
print('\n')


# ===== Swapping Keys and Values =====
data = {
    'a': 1,
    'b': 2    
}
swapped = {value: key for key, value in data.items()}
print(f'Comprehension:\t{swapped}')

swapped_dict = {}
for key, value in data.items():
    swapped_dict[value] = key
print(f'Simple:\t\t{swapped_dict}')
print('\n')


# ===== Nested Dictionary Comprehension =====
table = {x: {y: x*y for y in range(1, 4)} for x in range(1, 4)}
print(f'Comprehension:\t{table}')

table = {}
for x in range(1,4):
    temp_dict = {}
    for y in range(1,4):
        temp_dict[y] = x*y
    table[x] = temp_dict
print(f'Simple:\t\t{table}')