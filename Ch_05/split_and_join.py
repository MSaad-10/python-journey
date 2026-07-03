'''
    - .split() and .join() are two extremely important string methods in Python.
        * split()       string →  list
        * join()        list   →  string
    - Basic Syntax:
        * string.split(separator)
        * separator.join(list) 
'''


# ===== .split() =====
text = "Out of the blue"
result = text.split()
print(result)
print('\n')


# ===== Using Comma (,) Separator =====
data = "apple,banana,mango"
result = data.split(",")
print(result)
print('\n')


# ===== Using Hiphen (-) Separator =====
date = "18-05-2026"
print(date.split("-"))
print('\n')


# -===== Works only with strings =====
name, age = input("Enter your name and age (comma separated): ").split(',')
print(f'Value:\t{name}\tType: {type(name)}\nValue:\t{age}\tType: {type(age)}')
print('\n')


# ===== .join() =====
words = ['Out', 'of', 'the', 'blue']
result = " ".join(words)
print(result)
print('\n')


# ===== Using Comma (,) as Joiner =====
talk = ['Python', 'is', 'fun']
print(','.join(talk))
print('\n')


# ===== Using Hiphen (-) as Joiner =====
message = ['New', 'World', "order"]
print('-'.join(message))
print('\n')


# ===== Works only with Strings =====
info = ['Saad', 20]   #❌ERROR: 20 is an integer
# print('.'.join(info))
info = ['Saad', str(20)]
print('.'.join(info))
print('\n')


# .split() and .join() together
text = "Python is awesome"
words = text.split()
result = "-".join(words)
print(result)