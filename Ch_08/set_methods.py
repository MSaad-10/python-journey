# ===== .add() =====
#   👉 Adds element in set
s1 = {1,2,3,4,5,6}
print(f'Original:\t{s1}')
s1.add(8)   
print(f'add(8):  \t{s1}')
s1.add(1)   # Already exists
print(f'add(1):  \t{s1}')
print('\n')


# ===== .update() =====
#   👉 Adds multiple elements at once
letters = {'s', 'a', 'd'}
print(f'Original:             \t{letters}')
letters.update(['m','u','h'])
print(f"update(['m','u','h']):\t{letters}")
print('\n')


# ===== .remove() =====
#   👉 Removes an element from set, KeyError if value not existed
nums = {1,2,3,4,5}
print(f'Original: \t{nums}')
nums.remove(3)
print(f"remove(3):\t{nums}")
# nums.remove(8)   # KeyError
print('\n')


# ===== .discard() =====
#   👉 Removes an element from set, NoError if value not existed
vowels = {'a','e','i','o','u'}
print(f'Original:    \t{vowels}')
vowels.discard('a')
print(f"discard('a'):\t{vowels}")
vowels.discard('z')   # NoError
print('\n')


# ===== .pop() =====
#   👉 Removes random element
even = {2,4,6,8}
print(f'Original:\t{even}')
even.pop()
print(f"pop():   \t{even}")
# even.pop(2)  # TypeError
print('\n')


# ===== .clear() =====
#   👉 Clears the whole set
odd = {1,3,5,7,9}
print(f'Original:\t{odd}')
odd.clear()
print(f'clear(): \t{odd}')
print('\n')


# ===== .union() =====
#   👉 Combines unique elements
a = {1, 2, 3}
b = {3, 4, 5}
print(f'Union:\t{a.union(b)}')
print('\n')


# ===== .intersection() =====
#   👉 Returns common elements
a = {1, 2, 3}
b = {3, 4, 5}
print(f'Intersection:\t{a.intersection(b)}')
print('\n')


# ===== .difference() =====
#   👉 Elements in first set but not second
a = {1, 2, 3}
b = {3, 4, 5}
print(f'Difference:\t{a.difference(b)}')
print('\n')


# ===== .symmetric_difference() =====
#   👉 Non-common elements only
a = {1, 2, 3}
b = {3, 4, 5}
print(f'Symmetric Difference:\t{a.symmetric_difference(b)}')
print('\n')


# ===== .issubset() =====
#   👉 Checks if all elements exist inside another set
x = {1, 2}
y = {1, 2, 3, 4, 5}
print(x.issubset(y))
print(y.issubset(x))
print('\n')


# ===== .issuperset() =====
#   👉 Checks if set contains another set completely
a = {1, 2, 3}
b = {3, 4, 5}
print(a.issuperset(b))
print('\n')


# ===== .isdisjoint() =====
#   👉 Checks whether two sets have NO common elements
a = {1, 2, 0}
b = {3, 4, 5}
print(a.isdisjoint(b))