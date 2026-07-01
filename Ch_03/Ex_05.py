'''
    COUNT NUMMBER OF OCCURANCES OF A LETTER IN STRING
        - Ask the name of a user
        - Print count of each letter
        - Example:  "Muhammad Saad"
            # M = 1
            # u = 1
            # h = 1
            # a = 4
            # m = 2
            # d = 2
            # '' = 1
            # S = 1
'''


# Solution01: Using Dictionary
chars = {}
name = input("Enter your name: ")
for ch in name:
    count = 0
    count = name.count(ch)
    chars[ch] = count
    if ch in chars.keys():
        continue
for key, value in chars.items():
    print(f"{key}: {value}")


# Solution02: Using Temporary Variable
name = input("Enter your name: ")
count = 0
temp_var = ""
while count < len(name):
    if name[count] not in temp_var:
        temp_var += name[count]
        print(f"{name[count]}: {name.count(name[count])}")
    count += 1