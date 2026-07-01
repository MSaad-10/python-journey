''' 
    - Logical operators are used to combine multiple conditions together.
    - Python has 3 main logical operators:
        Operator            Meaning
        and	                Both conditions must be True
        or	                At least one condition must be True
        not	                Reverses the result
'''


# 'and' Operator
age = 20
citizen = True
if age >= 18 and citizen:
    print("Eligible to vote")
else:
    print("Not Eligible to vote")


# 'or' Operator
day = "Sunday"
if day == "Saturday" or day == "Sunday":
    print("Weekend")


# 'not' Operator
is_logged_in = False
if not is_logged_in:
    print("Please login")


# Short-circuit Evaluation  --->  'or'
    # True or anything → stops early
x = 10
if x > 5 or x / 0 == 1:         # No Error  
    print("Condition is True")


# Short-circuit Evaluation  ---> 'and'
    # False and anything → stops early
x = 2
if x > 5 and x / 0 == 1:
    print("Hello")