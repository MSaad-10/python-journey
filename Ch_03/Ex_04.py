'''
    EXERCISE: SUM OF DIGITS
        - Ask user to input a number containing more than one digit i.e. 1256
        - Calculate 1+2+5+6 and print.
'''


# Using 'string'
num = input("Enter a number (greater than 9): ")
sum = 0
for ch in num:
    sum += int(ch)
print(f"Sum: {int(sum)}")


# Using 'integer'
num = int(input("Enter a number (greater than 9): "))
sum = 0
while num != 0:
    n = num%10
    num /= 10
    num = int(num)
    sum += n
print(f"Sum: {int(sum)}")


# Using 'while' Loop
num = input("Enter a number (greater than 9): ")
sum = 0
count = 0
while count < len(num):
    sum += int(num[count])
    count += 1
print(f"Sum: {int(sum)}")