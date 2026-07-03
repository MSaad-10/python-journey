# ===== Creating list using range() =====
numbers = list(range(1,11))
print(numbers)
print('\n')


# ===== Storing value popped by .pop() =====
scores = [42, 107, 5, 88]
num_popped = scores.pop()
print(f'List:      \t{scores}')
print(f'Popped Num:\t{num_popped}')
print('\n')


# ===== Passing List in a function =====
def negative_list(L):
    negative = []
    for i in L:
        negative.append(-i)
    return negative

nums = list(range(1,11))
print(negative_list(nums))