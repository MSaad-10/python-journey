'''
    - Define a function that
        * takes a number(n) as input
        * returns a dictionary containing cube of numbers from 1 to n
        * Example:
            Input: 3
            Output: {1:1, 2:8, 3:27} 
'''


def cube_finder(n):
    cubes = {}
    for i in range(1,n+1):
        cubes[i] = i**3
    return cubes

n = int(input("Enter a number: "))
print(f'Answer: {cube_finder(n)}')