'''
    - A tuple is an ordered collection of items that cannot be changed after creation.
    - Tuples are immutable.
'''


# ===== Simple Example =====
numbers = tuple(range(1,6))
print(numbers, '\n')


# ===== Tuples with Mixed Data Types =====
data = ('Saad', 20, True, 3.7)
print(data, '\n')


# ===== Tuple Indexing =====
fruits = ('apple', 'banana', 'peach')
print(fruits[1], '\n')


# ===== Tuple Slicing =====
vegies = ('potato', 'mint', 'tomato')
print(f'Original:  \t{vegies}')
print(f'vegies[:2]:\t{vegies[:2]}')
print(f'vegies[::-1]:\t{vegies[::-1]}')
print('\n')


# ===== Tuples are Immutable =====
# fruits[0] = 'orange'   #ERROR
print(fruits,'\n')


# ===== Creating Single-Element Tuple =====
y = (5)   # Wrong 
x = (5,)
word = ('String')
text = ('Tuple',)
print(f'{x}\t        {type(x)}') 
print(f'{y}\t        {type(y)}') 
print(f'{text}\t{type(text)}') 
print(f'{word}\t        {type(word)}') 
print('\n')


# ===== Tuple Packing & Unpacking =====
data = ('Saad', 20, 'Pakistan')
mixed = ('Hello', 30, 2.10)
name, age, country = data   
# string, value = mixed   #ERROR
print(f'{name} \t {age} \t {country}')
print('\n')


# ===== Looping through Tuple =====
nums = (1,2,3,4,5)
for i in nums:
    print(i, end=" ")
print('\n')
# while loop
j = 0 
while j<len(nums):
    print(nums[j], end=" ")
    j+=1
print('\n')


# ===== Tuple without Paranthesis =====
guitars = 'yamaha', 'baton rouge', 'taylor'
print(guitars)
print(type(guitars))
print('\n')


# ===== List inside Tuple =====
things = ('perfume', 'soap', 'wire', ['candy', 'beans', 'syrup'])
print(f'Original:           \t{things}')
things[3].pop()
print(f'pop[3]:             \t{things}')
things[3].append('chocolate')
print(f"append('chocolate'):\t{things}")