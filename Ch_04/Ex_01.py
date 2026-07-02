'''
    - Create a fuction that takes:
        * name of a user as input
        * prints the last character of name
'''


def show_last(name):
    print(name[-1])

name = input("Enter your name: ")
show_last(name)


'''
    - Create a function that:
        * takes a number as input
        * tells whether the number is even/odd
'''


def even_odd(num):
    if num%2 == 0:
        return 'Even'
    return 'Odd'

num = int(input(("Enter a number: ")))
print(even_odd(num))


'''
    - Create a function that:
        * takes a number as input
        * check whether it is even
        * returns True/False
'''


def is_even(num):
    return num%2 == 0

num = int(input("Enter a number: "))
print(is_even(num))