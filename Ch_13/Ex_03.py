'''
    - Define a function that
        * takes any no. of lists containing numbers.
        * for example: [1,2,3], [4,5,6], [7,8,9]
        * returns the average of numbers like:
            (1+4+7)/3, (2+5+8)/3, (3+6+9)/3
    - Try to perform this exercise in one line implementation.
'''


# ===== Simple Function Implementation =====
def average_func(*args):
    average = []
    for pairs in zip(*args):
        average.append(sum(pairs)/len(pairs))
    return average

l1 = [1,2,3]
l2 = [4,5,6]
l3 = [7,8,9]
result = average_func(l1,l2,l3)
print(result)
print('\n')


# ===== Lambda Function Implementation =====
l1 = [1,2,3]
l2 = [4,5,6]
l3 = [7,8,9]
result = lambda *args: [sum(pairs)/len(pairs) for pairs in zip(*args)]
print(result(l1,l2,l3))