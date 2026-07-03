'''
    - Define a function that:
        * takes a list of words as an argument
        * returns a list with reverse of every element in the passed list
        * Example:
            ['abc', 'tuv', 'xyz']   --->   ['cba', 'vut', 'zyx']
'''


def reverse_words (L):
    newL = []
    for i in L:
        newL.append(i[::-1])
    return newL

words =  ['abc', 'tuv', 'xyz']
print(reverse_words(words))