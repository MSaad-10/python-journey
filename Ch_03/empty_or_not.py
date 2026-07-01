''' 
    - Before checking whether something is empty or not keep in mind that Python treats empty collections/strings as False 
      and non-empty ones as True. 
'''

# Simple Example
name = input("Enter your name: ")
if name:
    print(f"Your name is {name}")
else:
    print(f"You did\'nt enter anything!!")


# Checking Empty String
text = " "
if text:
    print('Not Empty')
else:
    print('Empty')


# Checking Empty List
num = []
if num:
    print('Not Empty')
else:
    print('Empty')


# Checking Empty Dictionary
student = {}
if student:
    print("Not Empty")
else:
    print("Empty")


# Using 'not' Operator
if not student:         # True when empty
    print("Dictionary is empty")
else:
    print("Dictionary is not empty")