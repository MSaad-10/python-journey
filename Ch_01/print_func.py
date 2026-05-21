print('hello world')    # used 'single quotes' because 'hello world' is a string
print("hello world")    # used "double quotes" because "hello world" is a string

print('a')              # used 'single quotes' because 'a' is a character
print("a")              # used "double quotes" because "a" is a character

print(5)                # 5 is an integer therefore no single or double quotes required
print(3.14)             # 3.14 is a float therefore no single or double quotes required

# It's OK to use 'single quotes' inside "double quotes"
print("hello 'beautiful' world")
# can't use "double quotes" inside "double quotes"
# print("hello "ugly" world")   ❌
# print("hello \"ugly\" world")  ✅
# print('I'm Saad')   ❌ERROR: This will cause a SyntaxError
print('I\'m Saad')    # ✅ Using the escape character '\'

# It's OK to use "double quotes" inside 'single quotes'
print('hello "beautiful" world')
# can't use 'single quotes' inside 'single quotes'
# print('hello 'ugly' world')   ❌
# print('hello \'ugly\' world')   ✅
