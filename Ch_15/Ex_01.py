'''
    - Define a generator function that:
        * takes an integer as argument
        * generates a sequence of even numbers from 1 to that integer
'''


def generator(num: int):
    yield from range(2, num+1, 2)

for i in generator(11):
    print(i)