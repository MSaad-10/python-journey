'''
    - Define a function that:
        * takes two lists as input
        * returns a list that contains elements that are common in both lists
        * Example:
            Input:   [1,2,5,8], [1,2,7,6]
            Output:  [1,2]
'''


# ===== Solution1 =====
def common_elements(l1,l2):
    common = []
    for i in l1:
        for j in l2:
            if i==j:
                common.append(i)
    return common

num1 = [1,2,5,8]
num2 = [1,2,7,6]
print(common_elements(num1,num2))
print('\n')


# ===== Solution2 =====
def common_elements(l1,l2):
    common = []
    for i in l1:
       if i in l2:
           common.append(i)
    return common

num1 = [1,2,5,8]
num2 = [1,2,7,6]
print(common_elements(num1,num2))