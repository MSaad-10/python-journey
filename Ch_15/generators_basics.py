'''
    - A generator is a special type of function that produces values one at a time instead of returning all values at once.
    - The key difference is:
        * A normal function uses 'return'
        * A generator uses 'yield'
    - yield is similar to return, but with one huge difference.
        * 'return' ends the function forever.
        * 'yield' pauses the function, remembers the current position and continues later.
    
'''


# ============= Difference b/w Function & Generator =============
def normal_func():
    return [1,2,3]

print(normal_func())       # Everything is created before anything is returned.

def generator():
    yield 1
    yield 2
    yield 3

print(generator())        # Calling a generator function does not execute it immediately.
gen = generator()
print(next(gen))
print(next(gen))
print(next(gen))          # Each call to next() asks the generator for the next value.
# print(next(gen))          # StopIteration
print()


# ============= What does 'yield' do? =============
def yield_demo():
    print('A')
    yield 1
    print('B')
    yield 2
    print("C")

gen = yield_demo()
print(next(gen))
print(next(gen))        # 'C' not printed because function pauses after every 'yield'
print()


# ============= Using Generator in for Loop =============
def gen_numbers():
    yield 'ali'
    yield 'sara'
    yield 'asad'

for number in gen_numbers():    # for loop automatically calls next() until the generator is exhausted.
    print(number)
print()


# ============= Generator with a Loop =============
def gen_count(n):
    for i in range(1,n+1):
        yield(i)
 
for num in gen_count(5):
    print(num)
print()


# ============= Memory Advantage =============
numbers = list(range(1000000))      # Python creates one million integers in memory at once.

def generator():
    for i in range(1000000):        # Python creates only one integer at a time (memory usage stays very small)
        yield i


# ============= Generator Expressions =============
list_comprehension = [x*x for x in range(5)]
print(list_comprehension)

gen_comprehension = (x*x for x in range(5))
print(gen_comprehension)                  # Prints the generator object
for square in gen_comprehension:
    print(square)
print()


# ============= Real-World Example =============
# Without generators:
with open("file.txt") as file:
    lines = file.readlines()        # loads the entire file into memory.
print(lines, '\n')

# With generators:
def read_file(filename):
    with open(filename) as file:
        for line in file:
            yield line              # only one line is kept in memory at a time.

for line in read_file('file.txt'):
    print(line.strip())
print()


# ============= Infinite Generator =============
def infinite_gen():
    num = 1
    while True:
        yield num
        num += 1

g = infinite_gen()
print(next(g))
print(next(g))
print(next(g))      # generator never ends unless you stop requesting values.
print()


# ============= yield from =============
def letters():
    yield 'A'
    yield 'B'

def combined():
    yield from letters()    # 'yield from' delegates yielding values from another iterable or generator.
    yield 'C'
    yield 'D'

for char in combined():
    print(char)
print()


# ============= Generators are One-Time Use =============
def numbers(n):
    for i in range(1, n+1):
        yield i

nums = numbers(10)      # Generator Object
for i in nums:
    print(i)

for i in nums:      # No Output: as generator is an iterator so it get exhausted 
    print(i)
