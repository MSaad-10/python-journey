'''
    ===== What is an Iterable? =====
    - An iterable is any object that can be iterated (looped over) one element at a time.
    - Examples of Iterables:
        * List
        * Tuple
        * String
        * Dictionary
        * Set
        * Range
'''


# ===== Basic Example =====
numbers = [10,20,30]
for num in numbers:     # numbers is an iterable
    print(num)
print('\n')


'''
    ===== What is an Iterator? =====
    - An iterator is an object that keeps track of the current position while iterating through an iterable.
    - It returns one element at a time.
    - Every Iterable can be converted to Iterator using iter() function.
    - Examples of Iterators:
        * map()
        * filter()
        * zip()
        * enumerate()
'''


# ===== Creating an Iterator =====
numbers = [1,2,3,4,5,6,7,8]
it = iter(numbers)      # iterator created
print(it)       # iterator object
print('\n')


# ===== Getting Elements from an Iterator =====
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it))    #ERROR: out of range
print('\n')


# ===== for Loop uses Iterators Internally =====
names = ['ali', 'saad', 'mark', 'bill', 'aliyan']
it = iter(names)
while True:
    try:
        name = next(it)
        print(name)
    except StopIteration:
        break
print('\n')


# ===== Are all Iterables are Iterators? =====      'NO'
numbers = [1,2,3]
# print(next(numbers))    #ERROR: TypeError


# ===== Are all Iterators are Iterables? =====      'YES'
nums = [1,2,3,4,5,6,7,8,9,10]
evens = filter(lambda x:x%2==0, nums)   # Iterator
for n in evens:
    print(n, end=" ")
print('\n')


# ===== One-time Nature of Iterators =====
digits = [0,1,0,0,1]
it = iter(digits)
print(list(it))
print(list(it))     # iterator has already been exhausted