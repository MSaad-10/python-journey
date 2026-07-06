'''
    - A frozenset is an immutable version of a normal set.
    - A frozenset cannot be chnaged (add/remove) after creation. 
'''


# ===== Simple Example =====
fset = frozenset([1,2,3])
# fset.add(4)   # AttributeError
print(fset)
print('\n')


# ===== Difference b/w Normal & Frozen =====
# ----------------------------------- #
# Normal Set
a = {1,2,3}
# b = {a}   # TypeError
# print(b)
print('\n')

# Frozen Set
a = frozenset([1,2,3])
b = {a,4,5}
print(b)
# ----------------------------------- #
print('\n')


# ===== Methods in frozneset =====

# ===== .copy() method =====
#   👉 Creates a copy of the frozenset
a = frozenset([1,2,3,4,5])
b = a.copy()
print(f'A = {a}\nB = {b}')
print('\n')

# ===== .union() method =====
#   👉 Combines unique elements from both sets
a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])
result = a.union(b)
print(f'Union:\t{result}')
print('\n')

# ===== .intersection() method =====
#   👉 Returns common elements only
a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])
result = a.intersection(b)
print(f'Intersection:\t{result}')
print('\n')

# ===== .difference() method =====
#   👉 Returns elements present in first set but not second
a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])
result = a.difference(b)
print(f'Difference:\t{result}')
print('\n')

# ===== issubset() method =====
#   👉 Checks whether all elements of one set exist inside another set
a = frozenset([1, 2])
b = frozenset([1, 2, 3, 4])
print(a.issubset(b))
print(b.issubset(a))
print('\n')

# ===== issuperset() method =====
#   👉 Checks whether set contains ALL elements of another set
a = frozenset([1, 2, 3, 4])
b = frozenset([1, 2])
print(a.issuperset(b))
print(b.issuperset(a))