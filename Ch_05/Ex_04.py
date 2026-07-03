'''
    - Define a function that:
        * filters even and odd numbers
        * returns a list that contains two lists: one with even & one with odd numbers
        * Example:
            [1,2,3,4,5,6,7]   --->   [[1,3,5,7], [2,4,6]] 
'''


def odd_even(L):
    odd = []
    even = []
    for i in L:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    mix = [odd,even]
    return mix

nums = [1,2,3,4,5,6,7]
print(odd_even(nums))