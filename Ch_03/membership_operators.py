''' 
    - The 'in' keyword is used to check whether a value exists inside a sequence or collection.
    - The 'not in' keyword is used to check whether a value does exist inside a sequence or collection.
'''


# 'in' with Strings
text = "Python"
print("p" in text)
print("P" in text)   # case sensitive
print('s' in 'saad')


# Checking Words
sentence = "I love Python"
print("Python" in sentence)


# 'in' with Lists
numbers = [1, 2, 3, 4]
print(3 in numbers)
print(10 in numbers)


# 'in' with Tuples
data = (10, 20, 30)
print(20 in data)


# 'in' with Sets
fruits = {"apple", "banana"}
print("apple" in fruits)
print("a" in fruits)


# 'in' with Dictionaries
student = {
    "name": "Saad",
    "age": 20
}
print("name" in student)
print("Saad" in student)    # checks only keys
print(20 in student.values()) # checks values
print(("name","Saad") in student.items())   # checks key-value pairs


# 'not in' Keyword
text = "Python"
print("z" not in text)