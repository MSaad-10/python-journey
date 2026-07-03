'''
    - min() and max() are built-in Python functions used to find:
        * smallest value
        * largest value
    from a collection of data.
'''


# ===== min() Function =====
#   👉 Finds the smallest element
numbers = [4, 1, 9, 2]
print(min(numbers))
print(min(2,5,0))   # multiple values directly
print('\n')


# ===== max() Function =====
#   👉 Finds the largest element
numbers = [4, 1, 9, 2]
print(max(numbers))
print('\n')


# ===== Using with List of Characters =====
#   👉 Compares characters alphabetically
letters = ['b', 'a', 'z']
print(f"Min: {min(letters)}")
print(f"Max: {max(letters)}")
print('\n')


# ===== Using with String Directly =====
text = "Python"
print(f"Min: {min(text)}")
print(f"Max: {max(text)}")
print('\n')


# ===== Using with Lists of Strings =====
fruits = ["apple", "banana", "mango"]
print(f"Min: {min(fruits)}")
print(f"Max: {max(fruits)}")
print('\n')


# ===== Mixed incompatible types can't be compared =====
data = [1, "apple", 3]   #ERROR: mixed elements
print(min(data))


# ===== Using 'key' Parameter =====
words = ["python", "AI", "coding"]
print(min(words, key=len))   # finds shortest word
print(max(words, key=len))   # finds longest word