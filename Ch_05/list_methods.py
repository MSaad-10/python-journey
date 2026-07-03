# ===== .count() =====
    # 👉 Counts occurrences of an element in a list
animals = ['panther', 'penguin', 'capybara', 'dolphin', 'dolphin']
print(animals.count('dolphin'))
print(animals.count('dog'))

# ===== .sort() =====
    # 👉 Sorts the original list
colors = ['crimson', 'teal', 'lavender', 'charcoal']
colors.sort()
print(colors)
    # 👉 Descending Sort
scores = [42, 107, 5, 88]
scores.sort(reverse=True)
print(scores)
    # 👉 .sort() modifies original list and returns None
temperatures = [98.6, 100.4, 97.2, 99.1]
result = temperatures.sort()
print(result)

# ===== sorted() function =====
    # 👉 Makes no changes to original
ratings = [4.8, 3.2, 4.9, 4.1]
print(f"Sorted: {sorted(ratings)}")
print(f"Original: {ratings}")
    # 👉 Returns a NEW sorted list
numbers = [4, 1, 3, 2]
new_list = sorted(numbers)   # returns sorted list
print(f'Sorted: {new_list}')
print(f'Original: {numbers}')

# ===== .reverse() =====
    # 👉 Reverses original list order
numbers = [1, 2, 3, 4]
print(f'Original: {numbers}')
numbers.reverse()
print(f'Reverse: {numbers}')
    # 👉 .reverse() only chnages order, does not sort
numbers = [3, 1, 4]
print(f'Original: {numbers}')
numbers.reverse()
print(f'Reverse: {numbers}')

# ===== .copy() =====
    # 👉 Creates a shallow copy of list
c = ['Tokyo', 'Paris', 'Nairobi', 'Lima']
b = c.copy()
print(b)
    # 👉 Without .copy() method
a = [1,2,3,4]
b = a   # both points to same list
b.append(5)
print(f'A: {a}')
print(f'B: {b}')
    # 👉 Independent copy
a = [1, 2, 3]
b = a.copy()
b.append(4)
print(f'A: {a}')
print(f'B: {b}')

# ===== .index() =====
    # 👉 Find the position (index) of an element in a list.
fruits = ['banana', 'apple', 'mango']
print(fruits.index('apple'))

    # 👉 .index() returns only first matching index
num = [1,2,3,4,5,6,1]
print(num.index(1))

    # 👉 Using start and end position:   list.index(value,start,end)
scores = [21,55,70,55,98,55,90,91,34,55]
print(scores.index(55,4,8))

    # 👉 Safe way to print if value not found
if 100 not in scores:
    print("Not Found")
else:
    print(scores.index(10))
   