'''
    - Following operations are applicable on set:
        1. Union        (|)
        2. Intersection (&)
        3. Difference   (-)
        4. Symmetric Difference (^)
        5. Frozen Set
'''


# Union (|) : Combines all unique elements
A = {1,2,3}
B = {4,5,6}
print(f'Union:\t{A|B}')
print('\n')


# Intersection (&) :  Common elements only
A = {1,2,3}
B = {4,5,6}
print(f'Intersection:\t{A&B}')
print('\n')


# Difference (-) : Elements in first set but not second
C = {1,2,3,4,5}
D = {3,5}
print(f'Difference:\t{C-D}')
print('\n')


# Symmetric Difference (^) : Elements NOT common in both
E = {1,4,6,8,3,2}
F = {23,5,2,7,9,21}
print(f'Symmetric Difference:\t{E^F}')