''' 
    - while loop means keep repeating code WHILE a condition remains True. 
    - while loop is best when you do NOT know exactly how many times repetition is needed.
'''


# Simple Example
count = 1
while count<=10:
    print(f"{count}. Hello World")
    count += 1


# User-Input Example
password = ""
while password != "saad123":
    password = input("Enter password: ")
    if password != "saad123":
        print("Wrong Password!")
print("Access granted!")


# Using 'break'
while True:
    text = input("Type 'exit' to stop: ")
    if text == "exit":
        break       # 'break' immediately stops the loop


# Using 'continue'
count = 0
while count<5:
    count += 1
    if count == 3:
        continue
    print(count)


''' =========== USE CASES =========== '''

# Menu Systems
print("1. Start")
print("2. Exit")
flag = True
while flag:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("System Started!!")
    elif choice == 2:
        print("Exit Successfully!!")
        flag = False
    else:
        print("Invalid Input!!")