'''
    - Print the following nested list using comprehension and for loop:
    - Example = [[1,2,3],[1,2,3],[1,2,3]]
'''


# ===== Comprehension =====
list_comp = [[j for j in range(1,4)] for i in range(3)]
print(f'Comprehension:\t{list_comp}')


# ===== for Loop =====
new_list = []
for i in range(3):
    row = []
    for j in range(1,4):
        row.append(j)
    new_list.append(row)

print(f'Simple:\t\t{new_list}')