''' 
    - Ask user to input 3 numbers and print average of 3 numbers using string formatting 
'''

# simple solution
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print(f"Average: {(a+b+c)/3}")

# input in one line
a,b,c = input("Enter three numbers (comma separated): ").split(",")
print(f"Average: {(int(a)+int(b)+int(c))/3}")