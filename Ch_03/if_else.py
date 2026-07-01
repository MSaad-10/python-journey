'''
    - An if-else statement is used to make decisions in Python.
    - It allows your program to do something if a condition is TRUE, otherwise do something else.
    - Syntax:
            if condition:
                # code runs if condition is TRUE
            else: 
                # code runs if condition is FALSE
'''

# Simple if_else
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to cast vote")
else:
    print("You aren't eligible to cast vote")


# Nested if_else
age = int(input("Enter your age: "))
is_citizen = int(input("Are you a citizen (0,1): "))
if age >= 18:
    if is_citizen:
        print("Eligible to cast vote")
    else:
        print("Not a citizen! \nIneligible to cast vote")
else:
    print("Ineligible to cast vote")