''' 
    - Prints series of fibonacci numbers.
'''


def fibonacci(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    elif n == 2:
        print(f"{a} {b}")
    else:
        print(f"{a} {b}", end = " ")
        for i in range(n-2):
            c = a + b
            a = b
            b = c
            print(b, end = " ")

num = int(input("Enter length of series: "))
fibonacci(num)