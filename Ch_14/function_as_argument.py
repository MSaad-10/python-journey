# ===== Using map() Function =====
l1 = [1,2,3,4,5]
print(f'Map Implementation:\t{list(map(lambda a: a**2, l1))}')


# ===== Using Simple Function =====
def my_map(func, l):
    new_list = []
    for item in l:
        new_list.append(func(item))
    return new_list

l2 = [1,2,3,4,5]
print(f'Simple Function:\t{my_map(lambda a: a**2, l2)}')


# ===== Using List Comprehension =====
def my_map2(func,l):
    return [func(item) for item in l]

l3 = [1,2,3,4,5]
print(f'List Comprehension:\t{my_map2(lambda a: a**2, l3)}')