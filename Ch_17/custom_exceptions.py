"""
    Python Custom Exceptions
        -Q: Why custom exceptions?
        -A: To increase the readability of code. 
"""


# ============= Example 1 =============
class InsufficientBalanceError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance")
    return balance - amount

withdraw(1000, 5000)
print('*'*40)


# ============= Example 2 =============
class NameTooShortError(ValueError):
    pass

def validate(name: str):
    if len(name)<8:
        raise NameTooShortError('Name is too short')
    
while True:
    try:
        username = input('Enter name: ')
        validate(username)
        print(f'Hello {username}')
        break
    except NameTooShortError as e:
        print(f"Error: {e}. Please try again.")

print('*'*40)