'''
    - Lists comparsion can be made in two ways:
        * '==' operator
        * 'is' keyword
'''


# '==' operator
#   👉 Does both lists contain the same values in same order?
a = [1, 3, 2]
b = [1, 2, 3]
print(a == b)
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print('\n')


# 'is' keyword
#   👉 Are both variables pointing to the exact same object in memory?
a = [100,200,300]
b = [500,600,700]
print(a is b)
b = a   # both points to same memory location
print(a is b)
