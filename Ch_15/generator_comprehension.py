'''
    - A generator comprehension is a compact way to create a generator without writing a full generator function.
'''


# ============= Difference b/w List & Generator Comprehension =============
list_comprehension = [i**2 for i in range(1,11)]
gen_comprehension = (i**2 for i in range(1,11))

print(type(list_comprehension))
print(type(gen_comprehension))

print(list_comprehension)
print(gen_comprehension)        # No element generated only Generator object
print()


# ============= Using for loop =============
numbers = (x for x in range(5))

for num in numbers:
    print(num)

for num in numbers:     # Generator Exhausted
    print(num)
print()


# ============= Using Condition =============
evens = (x for x in range(11) if x%2==0)
for n in evens:
    print(n)
print()


# ============= Nested Loops =============
pairs = ((x,y) for x in range(2) for y in range(2))

for pair in pairs:
    print(pair)
print()


# ============= Real-World Example =============
files = ['notes.txt', 'photo.jpg',  "report.txt", "music.mp3"]
txt_files = (file for file in files if file.endswith('.txt'))

for file in txt_files:
    print(file)