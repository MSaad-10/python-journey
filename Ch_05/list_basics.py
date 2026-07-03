''' 
    - A list is a collection of multiple items stored in a single variable.
    - We can store anything in lists like integer, float, string or another list.
    - Lists are mutable (can be changed).
'''

# ===== Simple Example =====
nums = [1,2,3,4]
print(nums)


# ===== Mixed data types =====
mixed = ["Saad", 20, True, 2.5, None, [3.78, 3.76, 3,58]]
print(mixed)


# ===== List Indexing =====
fruits = ["apple", "banana", "mango"]
print(fruits[0])
print(fruits[1])


# ===== Negative Indexing =====
vegies = ['onion', 'chili', 'garlic']
print(vegies[-1])


# ===== List Slicing =====
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])
mixed = [1, 2, 3, 4, 'five', 'six', 2.3, None]
mixed[5:] = 'assignment'
print(mixed)


# ===== Lists are Mutable =====
Fruits = ["apple", "banana"]
Fruits[0] = "mango"
print(Fruits)


# ===== Looping Through List =====
    # 👉 for loop
items = ['watch', 'ball', 'mouse']
for item in items:
    print(item, end=" ")
print('\n')
    # 👉 while loop
i = 0
while i < len(items):
    print(items[i], end=" ")
    i += 1
print('\n')


# ===== Membership Check =====
    # 👉 'in' keyword
vocab = ['abash', 'acclimate', 'aboriginal']
print("abash" in vocab)
    # 👉 'not in' keyword
dishes = ['pizza', 'sushi', 'tacos']
if 'ramen' not in dishes:
    print('Ramen not present')
else:
    print('Ramen present')


# ===== Nested Lists =====
matrix = [[1, 2], [3, 4]]
print(matrix[0])
print(matrix[0][1])
    # 👉 iterate using for & while
for item in matrix:
    i = 0
    while i < len(matrix):
        print(item[i])
        i += 1
    # 👉 iterate using nested for
for sublist in matrix:
    for i in sublist:
        print(i)