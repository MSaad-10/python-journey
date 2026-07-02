'''
    - Create a function that:
        * takes two numbers as input
        * tells which number is greater
'''


def greater(num1, num2):
    if num1 > num2:
        return f'{num1} is greater'
    return f'{num2} is greater'

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
print(greater(n1,n2))


'''
    - Create a function that:
        * takes three numbers as input
        * tells which number is greatest
'''


# Solution1
def greatest(n1, n2, n3):
    if (n1>n2) and (n1>n3):
        return f'{n1} is greatest'
    elif (n2>n1) and (n2>n3):
        return f'{n2} is greatest'
    elif (n3>n1) and (n3>n2):
        return f'{n3} is greatest'
    else:
        return 'All are equal'

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))
print(greatest(n1,n2,n3))

# Solution2
def greater(n1,n2):
    if n1>n2:
        return n1
    else:
        return n2
def greatest(n1,n2,n3):
    great = greater(n1,n2)
    return greater(great,n3)    # OR return greater(greater(n1,n2),n3)

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))
print(greatest(n1,n2,n3))