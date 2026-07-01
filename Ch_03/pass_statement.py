'''
    - The pass statement in Python means "Do nothing for now".
    - It is used as a placeholder when Python expects a block of code, but you don't want to write anything yet.
'''

# ERROR
# if True:
    # empty ❌

# CORRECT
if True:
    pass

''' =========== USE CASES =========== '''

# Simple Use
age = int(input("Enter your age: "))
if age >= 18:
    pass
else:
    print("Not eligible")


# Placeholder in Loops
for i in range(5):
    pass


# During Development
user_loged_in = True
if user_loged_in:
    pass        # will add login logic later