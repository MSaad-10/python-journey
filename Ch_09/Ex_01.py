'''
    - Define a function that:
        * takes a list of strings as input
        * returns the list of reverse strings as output
        * Use List Comprehension to perform this task
    - Example:
        Input:  l = ['abc', 'efg', 'hij']
        Output: l = ['cba', 'gfe', 'jih']
'''


def reverse_str(l):
    reverse_l = [string[::-1] for string in l]
    return reverse_l

l = ['abc', 'efg', 'hij']
print(reverse_str(l))