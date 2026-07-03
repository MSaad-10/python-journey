'''
    - Some main methods to add data in a list are:
        1. .extend()
        2. .append()
        3. .insert()
'''


# ===== .append() =====
    # Adds single item or list at end.
vegies = ['chili','tomato']
vegies.append('cucumber')
print(vegies)
fruits = ['mango', 'apple']
vegies.append(fruits)
print(vegies)


# ===== .insert() =====
    # Adds item before specific index.
fruits = ['mango', 'apple']
fruits.insert(2,'grapes')
print(fruits)
fruits.insert(-1, 'kiwi')
print(fruits)


# ===== .extend() =====
    # Adds multiple items in the form of other list.
f1 = ['mango','peach','dragon fruit']
f2 = ['guava','banana','cherry']
f1.extend(f2)
print(f1)


# ===== concatenation (+) =====
f1 = ['mango','peach','dragon fruit']
f2 = ['guava','banana','cherry']
fall = f1+f2
print(fall)