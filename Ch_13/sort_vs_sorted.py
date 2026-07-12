'''
    - In List, we use .sort() method to sort elements.
    - While sorted() function is used to return a  new sorted list from any iterable (list, tuple, set, dictionary, string, etc.).
    - list.sort() returns None and make changes to the original list.
    - While sorted() returns a list of sorted items and make no changes to original tuple, set or dictionary.
'''


# ===== .sort() in Lists =====
fruits = ['grapes', 'mango', 'apple']
print(f'Original:\t{fruits}')
print(fruits.sort())    # retruns 'None'
fruits.sort()           # sorts original
print(f'Updated:\t{fruits}')
print('\n')


# ===== sorted() with Tuples =====
fruits2 = ('grapes', 'mango', 'apple')
print(f'Original:\t{fruits2}')
print(f'Sorted:  \t{sorted(fruits2)}')   # returns sorted list
print(f'Original:\t{fruits2}')
print('\n')


# ===== sorted() with Sets =====
fruits3 = {'grapes', 'mango', 'apple'}
print(f'Original:\t{fruits3}')
print(f'Sorted:  \t{sorted(fruits3)}')  # returns sorted list
print(f'Original:\t{fruits3}')
print('\n')


# ===== Dictionaries inside List =====
guitars = [
    {'model': 'yamaha f310', 'price': 8400},
    {'model': 'faith naptune', 'price': 50000},
    {'model': 'faith apollo venus', 'price': 35000},
    {'model': 'taylor 814ce', 'price': 450000}
]
print(sorted(guitars, key = lambda item: item['price']))
print('\n')
print(sorted(guitars, key = lambda item: item['price'], reverse=True))
print('\n')


# ===== Sort by Lowercase =====
names = ['Ali', 'Zara', 'ahmad', 'saad']
print(sorted(names, key = str.lower))
print('\n')


# ===== Sorting by String Length =====
fruits = ["banana", "kiwi", "apple", "watermelon"]
print(sorted(fruits, key=len))
print('\n')


# ===== Sorting by Absolute Values =====
integers = [-10, 5, -3, 2, -11, 4]
print(sorted(integers, key = lambda x: abs(x)))
print('\n')


# ===== Sort by Multiple Fields =====
students = [
    ("Ali", 90),
    ("Ahmed", 90),
    ("Saad", 80),
    ("Bilal", 95)
]
print(sorted(students, key = lambda x: (x[1], x[0])))   # sort first by 'score' then by 'name'
print('\n')


# ===== Sorting Dictionaries =====
students = {
    "Ali": 90,
    "Saad": 75,
    "Ahmed": 95
}
print(sorted(students))     # sort by keys (names)
print(sorted(students.items(), key = lambda item: item[1]))    # sort by values (marks)