''' 
    - A for loop is used to repeat code for each item in a sequence or collection.
'''


# Simple Example
name = "Saad"
for ch in name:
    print(ch)


# 'for' with Lists
numbers = [10, 20, 30]
for num in numbers:
    print(num)


# 'for' with range(stop)
for i in range(5):      # 0-4
    print(i)


# 'for' with range(start, stop)
for i in range(1, 6):   # 1-5
    print(i)


# 'for' with range(start, stop, step)
for i in range(0, 10, 2):   # 0-9
    print(i)


# Reverse Loop
for i in range(5, 0, -1):   # 5-1
    print(i)


# 'for' with Dictionary
student = {
    "name": "Saad",
    "age": 20
}
for key, value in student.items():
    print(f"{key}: {value}")
 

# Using 'break'
for i in range(10):
    if i == 5:
        break
    print(i)


# Using 'continue'
for i in range(1, 11):
    if i == 5:
        continue
    print(i)


# Sum of n Numbers
num = int(input("Enter the range of sum (number): "))
sum = 0
for i in range(num+1):
    sum += i
print(f"Sum: {sum}")


# Sum of Digits
num = input("Enter a number: ")
sum = 0
for i in num:
    sum += int(i)
print(f"Sum: {sum}")

# ==== ALTERNATIVE ====
add = 0
for i in range(len(num)):
    add += int(num[i])
print(f"Result: {add}")


# Number of Occurances of Charcters in a String
name = input("Enter your name: ")
temp_var = ""
for i in range(len(name)):
    if name[i] not in temp_var:
        print(f"{name[i]}: {name.count(name[i])}")
    temp_var += name[i]