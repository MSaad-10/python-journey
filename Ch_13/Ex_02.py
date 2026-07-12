'''
    - Take two lists of numbers.
    - For each element of two parallel lists check which number is greater and add it to the new list.
'''


l1 = [1,2,4,5,6]
l2 = [0,3,7,8,4]
new_list = []
for pair in zip(l1,l2):
    new_list.append(max(pair))

print(new_list)