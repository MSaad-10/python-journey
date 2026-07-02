'''
    - A function can return multiple values of different data types at once. 
'''


def func(int1, int2):
    sum = int1 + int2
    product = int1 * int2
    power = int1 ** int2
    return sum,product,power

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
print(func(n1,n2))
sum, product, power = func(n1,n2)
print(f'Sum: {sum}\nProduct: {product}\nPower: {power}')