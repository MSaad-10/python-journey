'''
    LETTER COUNTER DICTIONARY
    - Define a function that
        * takes a string as an input
        * returns the count of each letter in that string in the form of dictonary
    - Example:
        Input: "Saad"
        Output: {'S': 1, 'a': 2, 'd': 1}
'''


def counter(s):
    new_dict = {}
    for i in s:
        new_dict[i] = s.count(i)
    return new_dict

string = input("Enter a string: ")
print(counter(string))