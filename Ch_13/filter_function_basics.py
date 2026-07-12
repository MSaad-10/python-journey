''' 
    - filter() function is a built-in Python function that selects only those elements from an iterable that satisfy a given condition.
    - Think of it like a sieve:
        * map()     →   Transforms every element.
        * filter()  →   Selects only the elements that meet a condition i.e. function returns True/False.
    - Syntax:
                filter(function, iterable)
'''


# ===== Basic Example =====
def is_even(nums):
    return nums%2 == 0

numbers = [1,2,3,4,5,6,7,8,9,10]
evens = list(filter(is_even, numbers))
print(evens)
print('\n')


# ===== Using Lambda Function =====
numbers = [1,2,3,4,5,6,7,8,9,10]
odds = list(filter(lambda x:x%2!=0, numbers))
print(odds)
print('\n')


# ===== Filter Strings by Length =====
names = ["Ali", "Saad", "Ahmed", "A"]
result = list(filter(lambda name:len(name)>3, names))
print(result)
print('\n')


# ===== Filter Positive Numbers =====
numbers = [-5, 2, -1, 7, 0]
positive = list(filter(lambda x:x>0, numbers))
print(positive)
print('\n')


# ===== Filter a Dictionary =====
marks = {
    'student1': 76,
    'student2': 98,
    'student3': 65,
    'student4': 58
}

result = filter(lambda nums: nums[1]>85, marks.items())
print(dict(result))
print('\n')


# ===== filter() is an iterator =====
names = ['saad', 'asad', 'sameer', 'ali']
result = filter(lambda n:n.startswith('s'), names)
for name in result:         # filter() object can be iterated only once
    print(name, end=" ")
print('\n')


# ===== filter() object & iterable =====
nums = [1,2,3,4,5,6,7,8,9,10]
evens = filter(lambda a:a%2==0, nums)
even_nums  = [i for i in nums if i%2==0]
print(f'Filter Object:\t{evens}')
print(f'Iterable:     \t{even_nums}')
print('\n')


# ===== Filter Characters from a String =====
text = "Python123"
letters = list(filter(str.isalpha, text))
print(letters)
print('\n')


# ===== Using 'None' with filter() =====
data = [0, 1, "", "Hello", False, True, None, 25]
result = list(filter(None, data))    # 'None' will remove all falsy values
print(result)