'''
    - Define a function that will take list as an argument and will return a reversed list.
    - Example:
        [1,2,3,4]           -->   [4,3,2,1]
        ['word1','word2']   -->   ['word2', 'word1']
    - Solve this problem using:
        1. .append() and .pop() methods
        2. list slicing
        3. reverse method
'''


# ===== Solution1 =====
def rev(l):
    newl = []
    i = 0
    for i in range(len(l)):
        popped = l.pop()
        newl.append(popped)
    return newl

nums = [1,2,3,4]
print(rev(nums))
words =['word1','word2'] 
print(rev(words))
print('\n')


# ===== Solution2 =====
def rev(l):
    return l[::-1]

nums = [1,2,3,4]
print(rev(nums))
words =['word1','word2'] 
print(rev(words))
print('\n')


# ===== Solution3 =====
def rev(l):
    l.sort(reverse=True)
    return l

nums = [1,2,3,4]
print(rev(nums))
words =['word1','word2'] 
print(rev(words))