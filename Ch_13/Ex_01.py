'''
    - Define a function that takes two arguments:
        1. List containing strings
        2. String that you want to find in your List
    - Funtion will return the index of string in your list and if string not present then return -1
'''


def str_index(s,key):
    for pos, word in enumerate(s):
        if word == key:
            return pos
    return -1

words = ['ball', 'shuttle', 'racket', 'boots']
print(f'Index: {str_index(words,'snake')}') 