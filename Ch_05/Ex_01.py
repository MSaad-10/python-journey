'''
    - Define a function which will: 
        * take list containing numbers as user input
        * return  a list containing square root of that numbers
'''


def sqaure_root(L):
    sqrt = []
    for i in L:
        sqrt.append(i**2)
    return sqrt

nums = []
while -1 not in nums:
    n = int(input("Enter elements: "))
    nums.append(n)
nums.pop()
print(nums)
print(sqaure_root(nums))