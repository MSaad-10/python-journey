'''
    - The zip() function is used to combine two or more iterables element by element into a single iterator of tuples.
    - Example:
                    List 1: A     B     C 
                    List 2: 1     2     3 
                            |     |     |
                          (A,1) (B,2) (C,3)
    - Syntax:
                zip(iterable1, iterable2, iterable3, ...)
'''


# ===== Basic Example =====
user_id = ['user1', 'user2', 'user3']
names = ['saad', 'asad', 'ali']
zipped = zip(user_id, names)
print(f'Zip Object:\t{zipped}')
print(f'List:      \t{list(zipped)}')
print('\n')


# ===== Different Length Iterables =====
user_id = ['user1', 'user2', 'user3']
names = ['saad', 'asad']
print(list(zip(user_id, names)))      # third name is ignored bcz names has only two elements
print('\n')


# ===== Using zip() in a for loop =====
names = ["Ali", "Saad", "Ahmad"]
marks = [85,72,23]
for name, mark in zip(names, marks):
    print(name, "scored", mark)
print('\n')


# ===== Zipping Three Iterables =====
names = ["Ali", "Saad", "Ahmed"]
marks = [85, 92, 78]
grades = ["B", "A", "C"]
for name, mark, grade in zip(names, marks, grades):
    print(name, mark, grade)
print('\n')


# ===== Unzipping Data =====
students = [("Ali", 85), ("Saad", 92), ("Ahmed", 78)]
names, marks = zip(*students)
print(names)
print(marks)
print('\n')


# ===== Using zip() with Strings =====
word1 = "ABC"
word2 = "123"
print(list(zip(word1, word2)))
print('\n')


# ===== Using zip() with lists =====
list1 = [1,2,3]
list2 = ["a", 'b', 'c']
for number, letter in zip(list1, list2):
    print(number, letter)
print('\n')


# ===== zip() Returns an Iterator =====
numbers = [1,2,3,4,5]
letters = ['a','b','c','d','e']
z = zip(numbers, letters)
print(type(z))
print('\n')


# ===== Iterator Behavior =====
digits = [1, 2, 3]
characters = ["a", "b", "c"]
z = zip(digits, characters)
print(list(z))
print(list(z))      # iterator exhaustion
print('\n')


# ===== Creating a Dictionary with zip() =====
names = ["Ali", "Saad", "Ahmed"]
marks = [85, 92, 78]
student_marks = dict(zip(names, marks))
print(student_marks)