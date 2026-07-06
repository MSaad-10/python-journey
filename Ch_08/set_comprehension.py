'''
    - A set comprehension is a concise way to create a set using a loop and optional conditions.

'''


# ===== Squared Numbers =====
squares = set()
for i in range(1,6):
    squares.add(i**2)
print(f'Simple:\t\t{squares}')

squared_set = {i**2 for i in range(1,6)}
print(f'Comprehension:\t{squared_set}')
print('\n')


# ===== Removing Duplicates Automatically =====
numbers = [1,1,2,2,3,3,4,4,5,5]
uniques = set()
for num in numbers:
    uniques.add(num)
print(f'Simple:\t\t{uniques}')

unique_set = {num for num in numbers}
print(f'Comprehension:\t{unique_set}')
print('\n')


# ===== Even Numbers Only =====
evens = set()
for i in range(1,10):
    if i%2 == 0:
        evens.add(i)
print(f'Simple:\t\t{evens}')

even_set = {i for i in range(1,10) if i%2==0}   # if condition in set_comprehension
print(f'Comprehension:\t{even_set}')
print('\n')


# ===== Working with Strings =====
word = "Programming"
letters = set()
for ch in word:
    letters.add(ch)
print(f'Simple:\t\t{letters}')

letters_set = {ch for ch in word}
print(f'Comprehension:\t{letters_set}')
print('\n')


# ===== Converting Strings to Uppercase =====
names = ['saad', 'ali', 'hamza', 'asad']
capitals = set()
for name in names:
    capitals.add(name.upper())
print(f'Simple:\t\t{capitals}')

capitals_set = {n.upper() for n in names}
print(f'Comprehension:\t{capitals_set}')
print('\n')


# ===== Creating a Set of Lengths =====
animals = ['cat', 'dog', 'crocodile', 'tiger', 'lion']
length = set()
for animal in animals:
    length.add(len(animal))
print(f'Simple:\t\t{length}')

length_set = {len(an) for an in animals}
print(f'Comprehension:\t{length_set}')
print('\n')


# ===== Nested Set Comprehension =====
nested = set()
for x in range(1,4):
    nested.add(frozenset({x,x+1}))
print(f'Simple:\t\t{nested}')

nested_set = {frozenset({x,x+1}) for x in range(1,4)}
print(f'Comprehension:\t{nested_set}')
print('\n')


'''
        - A set can only contain hashable (immutable) objects. 
        - A normal set is mutable, so it cannot be an element of another set.
        - A frozenset can an element of set, so nested set are made using frozenset.
'''