'''
    - The any() and all() functions are built-in Python functions used to evaluate multiple Boolean values.
    - They are especially useful when working with:
        * Lists
        * Tuples
        * Sets
        * Dictionaries
        * Generators
        * Results from map() and filter()
    - any() returns TRUE if at least one element in the iterable is TRUE. If all elements are FALSE, it returns FALSE.
        * Syntax:       any(iterable)
    - all() returns TRUE only only if every element is TRUE. If even one element is FALSE, it returns FALSE.
        * Syntax:       all(iterable)
'''


# ===== Basic Example: any() =====
bool1 = [False, False, True, False]     # one TRUE
print(any(bool1))
bool2 = [False, False, False]       # all FALSE
print(any(bool2))
print('\n')


# ===== Basic Example: all() =====
bool1 = [True, True, True]     # all TRUE
print(all(bool1))
bool2 = [True, True, False]       # one FALSE
print(all(bool2))
print('\n')


# ===== Even Test: all() =====
numbers1 = [2,4,6,8,10]
numbers2 = [1,2,3,4,5,6]
evens1 = []
evens2 = []
for num in numbers1:
    evens1.append(num%2==0)
for num in numbers2:
    evens2.append(num%2==0)
print(evens1)        
print(all(evens1))   # to check whether all numbers are even or not, we will use all() which will give a single boolean value
print(evens2)
print(all(evens2)) 
print('\n')


# ===== Odd Test: any() =====
numbers3 = [2,4,5,8,10]
odds = []
for num in numbers3:
    odds.append(num%2!=0)
print(odds)
print(any(odds))
print('\n')


# ===== Working with Strings =====
words = ["Python", "", "AI"]
print(any(words))
print(all(words))
print('\n')


# ===== Working with Lists =====
lists = [[], [1], [1,2]]
print(any(lists))
print(all(lists))
print('\n')


# ===== Working with Conditions =====
marks = [45, 32, 76, 28]
result = any(mark>=50 for mark in marks)
print(result)
print('\n')


# ===== Using with map() =====
numbers = [1,2,3,4,5]
result = any(map(lambda x:x>3, numbers))
print(result)
print('\n')


# ===== Using with filter() =====
numbers = [1,2,3,4,5]
filtered = filter(lambda x:x>3, numbers)
print(f'{any(filtered)}')
print('\n')


# ===== Using with Dictionaries =====       
student = {
    'name': '',
    'age': 0
}
print(any(student))     # checks only the keys of the dictionary
print(any(student.values()))