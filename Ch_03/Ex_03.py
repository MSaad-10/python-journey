''' 
    EXERCISE: Calculate sum of first 20 numbers using 'while' loop.
'''


count = 1
sum = 0
while count <= 20:
    sum += count
    count += 1
print(f"Sum: {sum}")


''' 
    EXERCISE: Sum of n natural numbers  
        - Ask user to enter a natural number
        - Print total from 1 to n
'''


num = int(input("Enter a number: "))
count = 1
sum = 0
while count <= num:
    sum += count
    count += 1
print(f"Sum (1 to {num}): {sum}")