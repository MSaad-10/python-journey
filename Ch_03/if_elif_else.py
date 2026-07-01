'''
    - if-elif-else checks conditions one by one and execute the first matching block.
    - Syntax:
            if condition1:
                # code
            elif condition2:
                # code
            elif condition3:
                # code
            else:
                # code
            
'''

# Simple Example
age = int(input("Enter your age: "))
if age <= 0:
    print("You can't watch")
elif age < 4:                           # 1 to 3
    print("Ticket Price: Free")
elif age < 11:                          # 4 to 10
    print('Ticket Price: 150/-')
elif age < 61:                          # 11 to 60
    print("Ticket Price: 250/-")
else:                                   # above 60
    print("Ticket Price: 200/-")