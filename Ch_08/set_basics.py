'''
    - A set is an unordered collection of UNIQUE elements.
    - Any type of data can be stored in a set except List, Dictionary and Tuple.
'''


# ===== Simple Example =====
s1 = {1,2,4,5,6,78,3,2}
print(f'Original:\t{s1}')   
l1 = [1,2,4,4,6,6,3,6,46,2,4,1,5]
print(f'List:    \t{set(l1)}')   
t1 = (1,3,5,2,5,2,6,1,6,4,2,6,8,4,2,0)
print(f'Tuple    \t{set(t1)}')
s1 = "Muhammad Saad"
print(f'String:  \t{set(s1)}') 
print('\n')


# ===== Empty Set =====
empty = set()
print(f'Empty Set:\t{empty}')
print('\n')


# ===== Removing duplicates in a list =====
list1 = [1,2,2,2,3,4,5,6,6,6,7,3,5,7,2,8,9]
unique = list(set(list1))
print(f'Unique:\t{unique}')
print('\n')


# ===== Membership Check =====
words = {'hi','bye','hello'}
print('hi' in words)
print('no' in words)
print('\n')


# ===== Looping Through Set =====
german = {'ich', 'bin', 'alex'}
for words in german:
    print(words, end = " ")