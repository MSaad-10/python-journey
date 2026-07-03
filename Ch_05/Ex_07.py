'''
    - Define a function that:
        * takes a list with sublists as input
        * returns the number of sublists in the given list
        * Example:
            Input: [1,2,3, ['word1','word2'], 0.5]
            Output: 1
'''


def count_sublists(L):
    count = 0
    for i in L:
        if type(i) == list:
            count+=1
    return count

l = [1,2,3, ['word1','word2'], 0.5, [1,2,3,4]]
print(count_sublists(l))