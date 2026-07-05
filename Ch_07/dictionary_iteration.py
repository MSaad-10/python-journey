
# ===== Looping Through Dictionary =====
user_info = {
    'name' : 'Alex',
    'age'  : 30,
    'role' : 'AI Engineer',
    'salary':  1000000
}


# Keys
print(f'Keys:',end=" ")
for key in user_info:
    print(key, end = " ")
print('\n')


# Values
print(f'Values:',end=" ")
for value in user_info.values():
    print(value, end = " ")
print('\n')


# Both keys & values
print(f' Values & Keys')
for key, value in user_info.items():
    print(f'{key}:\t{value}')
print('\n')


# Printing key-value pairs
print(f' Key-Value Pairs')
for i in user_info.items():
    print(i) 
print('\n')


# Printing keys & values with iterator 'i'
for i in user_info:
    print(f'{i}:\t{user_info[i]}')