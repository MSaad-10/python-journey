'''
    - enumerate() is a built-in Python function that lets you loop through an iterable (like a list, tuple, or string) while also 
      keeping track of the index.
    - We use enumerate function with for loop to track position of our item in iterable.
'''


# ===== Without & with Enumerate Function =====
names = ['saad', 'ali', 'aliyan']
for i in range(len(names)):
    print(f'{i} ---> {names[i]}')
print('\n')

for p, n in enumerate(names):
    print(f'{p} ---> {n}')
print('\n')


# ===== Basic Usage =====
fruits = ['orange', 'apple', 'banana']
for index, fruit in enumerate(fruits):
    print(index, fruit)
print('\n')


# ===== Custom Starting Index =====
stationary = ['pen', 'eraser', 'marker']
for index, item in enumerate(stationary, start=1):
    print(index, item)
print('\n')


# ===== Enumerating a String =====
word = 'Abashed'
for index, char in enumerate(word):
    print(index, char)
print('\n')


# ===== Return Value of Enumerate =====
nums = ['one','two','three','four','five']
e = enumerate(nums,start=1)
print(e)            # memory address of enumerate object    
print(list(e))      # list containing (index, value) pairs