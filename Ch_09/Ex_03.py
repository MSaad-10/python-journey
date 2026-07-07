'''
    - Define a function that:
        * takes a list of numbers as input
        * returns a list of numbers which contains
            * negative of odds in that list and square of evens
        * Use List Comprehension for this task
    Example:
        Input:  [1,2,3,4,5,6,7,8,9,10]
        Output: [-1,2,-3,4,-5,6,-7,8,-9,10]
'''


# ===== Comprehension =====
def neg_pos(nums):
    return [i**2 if i%2==0 else -i for i in nums]

print(f'Comprehension:\t{neg_pos([1,2,3,4,5,6,7,8,9,10])}')


# ===== for Loop =====
def odd_even(nums):
    numbers = []
    for num in nums:
        if num%2 == 0:
            numbers.append(num**2)
        else:
            numbers.append(-num)
    return numbers

print(f'Simple:\t\t{odd_even([1,2,3,4,5,6,7,8,9,10])}')