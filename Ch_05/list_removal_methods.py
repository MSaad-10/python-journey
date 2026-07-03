'''
    - Some of the methods to remove data from a list are:
        * .pop()
        * del
        * .remove()
        * .clear()
'''


# ===== .pop() =====
#   👉 Removes by index.
animals = ['panther', 'penguin', 'capybara', 'dolphin']
print(f"Original:\t{animals}")
animals.pop()   # removes value at last index
print(f'pop():   \t{animals}')
animals.pop(0)  # removes value at 0th index
print(f'pop(0):   \t{animals}')
print('\n')


# ===== del operator =====
#   👉 Deletes the value at specific index
colors = ['crimson', 'teal', 'lavender', 'charcoal']
print(f"Original:\t{colors}")
del colors[3]
print(f'del[3]:   \t{colors}')
# del colors[5]   ❌ERROR
print('\n')


# ===== .remove() =====
#   👉 Removes by value.
languages = ['Python', 'Rust', 'Go', 'JavaScript']
print(f"Original:    \t  {languages}")
languages.remove('Python')
print(f"remove('Python'): {languages}")
# languages.remove('C#')   ❌ERROR: 'C#' doesn't exist
languages.append('Rust')
print(f"append('Rust'):   {languages}")
languages.remove('Rust')   # removes first 'Rust'
print(f"remove('Rust'):   {languages}")
# languages.remove('rust')   ❌ERROR: case sensitive
print('\n')


# ===== .clear() =====
    # Removes all items.
cities = ['Tokyo', 'Paris', 'Nairobi', 'Lima']
print(f"Original:\t{cities}")
cities.clear()
print(f'clear:   \t{cities}')