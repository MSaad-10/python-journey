'''
    - Define a function:
        * takes a list of strings as input.
        * returns list with first character of each string capitalized if only list is passed.
        * returns list with strings reversed and first character of reversed strings capitalized if list and 
          argument reverse_str = 'True' is passed. 
    - Example:
        name = ['saad', 'ali']
        Input:    func(name)                        Output:   ['Saad', 'Ali']
        Input:    func(name, reverse_str='True')    Output:   ['Daas', 'Ila']
'''


def func(name, reverse_str = False):
    if reverse_str:
        return [n[::-1].title() for n in name]
    return [n.title() for n in name]

name = ['saad', 'ali']
print(func(name))
print(func(name,True))
