'''
    - Define a function that:
        * takes a list of mixed data types as input
        * returns a list of numbers in previous list changed to string
    - Example:
        Input:  [True, False, 5, [1,2,3], "Hello", 6.5, 1, 0.5]
        Output: ['5', '6.5', '1', '0.5']
'''


# ===== Comprehension =====
def int_float(mixed):
    return [str(num) for num in mixed if (type(num) == int or type(num) == float)]

mixed = [True, False, 5, [1,2,3], "Hello", 6.5, 1, 0.5]
print(f'Comprehension:\t{int_float(mixed)}')


# ===== for Loop =====
def numbers(mixed):
    nums = []
    for num in mixed:
        if (type(num) == int or type(num) == float):
            nums.append(str(num))
    return nums

print(f'Simple:\t\t{numbers(mixed)}')