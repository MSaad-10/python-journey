'''
    - Define a function that:
        * takes a list as an input
        * retruns the difference of largest and smallest number
        * Example:
            Input:  [6,60,2]
            Output: 58
'''


def difference(L):
    return max(L) - min(L)

nums = [6,60,2]
print(f"Difference: {difference(nums)}")