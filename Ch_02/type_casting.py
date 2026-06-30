''' 
    - Type Casting or Type Conversion is the process of converting one data type into another.
'''

# int() function
print(int("10"), type(int("10")))
print(int(5.6), type(int(5.6)))
# int("10.5") ❌

# float() function
print(float("10"), type(float("10")))
print(float(5), type(float(5)))
print(float("3.14"), type(float("3.14")))

# str() function
print(str(10), type(str(10)))
print(str(3.14), type(str(3.14)))

age = 20
print("My age is " + str(age))

# bool() function
print(bool(0))
print(bool(""))
print(bool(None))
print(bool(1))
print(bool("Saad"))
print(bool(5))

# list() function
print(list("Saad"))
print(list((1,2,3)))   # tuple -> list

# tuple() function
print(tuple([1,2,3]))   # list -> tuple

# set() function
print(set([1,2,2,3,3]))  # list -> set

# dict() function
print(dict([("name","Saad"), ("age",20)]))  # list -> dictionary