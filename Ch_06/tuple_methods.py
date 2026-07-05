'''
    - Following are some methods and functions that Tuple supports:
        * methods
            1. .count()
            2. .index()
        * functions
            1. len()
            2. sum()
            3. min() & max()
            4. sorted()
            5. enumerate()
            6. any() & all()
            7. reversed()
'''


# ===== .count() =====
#   👉 Counts how many times an element appears
numbers = (1,2,2,2,2,3,4,5)
print(numbers.count(2))
print('\n')


# ===== .index() =====
#   👉 Finds position of first occurrence
numbers = (10,20,30,40,20)
print(numbers.index(20))
print(numbers.index(20,2,5))
print('\n')


# ===== len() =====
#   👉 Counts total elements
data = (1, 2, 3)
print(len(data))
print('\n')


# ===== min() & max() =====
#   👉 Find min & max element
numbers = (4,1,5,7,90)
print(f'Min: {min(numbers)}')
print(f'Max: {max(numbers)}')
print('\n')


# ===== sum() =====
#   👉 Adds numeric values
values = (1,5,7,2)
print(sum(values))
print('\n')


# ===== sorted() =====
#   👉 Returns sorted list
digits = (2,6,1,7,9,0)
print(sorted(digits))
print(tuple(sorted(digits)))
print('\n')


# ===== any() =====
#   👉 Returns TRUE if at least one item is TRUE.
data = (0,False,-1)
print(any(data))
print('\n')


# ===== all() =====
#   👉 Returns TRUE if all values are TRUE.
values = (1,4,True,'Ali',None)
print(all(values))
print('\n')


# ===== enumerate() =====
#   👉 Adds index number with values
fruits = ("apple", "banana")
for index, value in enumerate(fruits):
    print(index, value)
print('\n')


# ===== reversed() =====
#   👉  reverses the tuple
numbers = (1,4,6,1,49)
print(tuple(reversed(numbers)))
print('\n')    