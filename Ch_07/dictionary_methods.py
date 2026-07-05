# ===== .values() =====
student = {
    "name": "Saad",
    "age": 20,
    "city": "Lahore"
}
values = student.values()
print(values,'\t',type(values))
print('\n')


# ===== .keys() =====
student = {
    "name": "Saad",
    "age": 20,
    "city": "Lahore"
}
keys = student.keys()
print(keys,'\t',type(keys))
print('\n')


# ===== .items() =====
student = {
    "name": "Saad",
    "age": 20,
    "city": "Lahore"
}
items = student.items()
print(items,'\t',type(items))
print('\n')


# ===== .update() =====
user_info =  {
    'name': 'saad',
    'age': 24,
    'cgpa': 3.58
}
more_info = dict(city = 'Lahore', name = 'Ali', salary = 1000)    
user_info.update(more_info)     # 'name' will be changed in user_info
print(f'Original:\t{user_info}')
user_info.update({})   # no updation
print(f'No Updation:\t{user_info}')
user_info.update({
    'caste' : 'Sardar',
    'religion': 'Islam'
})
print(f'Updated:\t{user_info}')
print('\n')


# ===== .fromkeys() =====
#   👉 Creates new dictionary using keys.
dic = dict.fromkeys(['name', 'city', 'gpa'], 'unknown')   # using List
print(f'Using List:\t{dic}')
dic = dict.fromkeys(('name', 'city'), ['unknown','unknown'])   # using Tuple
print(f'Using Tuple:\t{dic}')
dic = dict.fromkeys("abcd", 'unknown')   # using String
print(f'Using String:\t{dic}')
dic = dict.fromkeys(range(1,6), 'unknown')   # using range() function
print(f'Using range():\t{dic}')
print('\n')


# ===== .get() =====
#   👉 Safely gets value from key
student = {
    'name' : 'asad',
    'cgpa': 3.78,
    'marks': 67
}
print(f"get('name'):   \t{student.get('name')}")
print(f"get('roll_no'):\t{student.get('roll_no')}")   # by default 'None'
print(f"get('class'):  \t{student.get('class','Not Found')}")   # returns 'Not Found' if key not available
print('\n')


# ===== .copy() method =====
#   👉 Creates copy of dictionary
item_dict = dict(item_name = "Clock", item_no = 120)
backup_item = item_dict.copy()   # creates copy
print(f'(item_dict == backup_item):\t{item_dict == backup_item}')
print(f'(item_dict is backup_item):\t{item_dict is backup_item}')
print(f'Item:\t\t\t\t{item_dict}\nBackup:\t\t\t\t{backup_item}')
print('\n')

backup_item = item_dict   # both points to same memory location
print(f'(backup_item is item_dict):\t{backup_item is item_dict}')
print(f'(backup_item == item_dict):\t{backup_item == item_dict}')
backup_item['price'] = 1500
print(f'Item:\t\t\t\t{item_dict}\nBackup:\t\t\t\t{backup_item}')
print('\n')


# ===== .setdefault() method =====
#   👉 Gets value if key exists otherwise creates key with default value
car = dict(manufacturer = "Honda", model = 2026)
print(f'Original:\t\t\t{car}')
car.setdefault('model',1000)   # key exists
print(f"setdefault('model',1000):\t{car}")
car.setdefault('price',1000)   # creates new key 'price'
print(f"setdefault('price',1000):\t{car}")


'''

--Dictionary Methods Summary Table---
| Method        | Purpose           |
| ------------- | ----------------- |
| .keys()       | get keys          |
| .values()     | get values        |
| .items()      | get pairs         |
| .get()        | safe access       |
| .update()     | update dictionary |
| .pop()        | remove item       |
| .popitem()    | remove last item  |
| .clear()      | empty dictionary  |
| .copy()       | copy dictionary   |
| .setdefault() | add default value |
| .fromkeys()   | create new dict   |

'''
