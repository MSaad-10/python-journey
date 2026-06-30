'''
    - Take user's name as input and add 4 stars on both sides of name
'''

name = input("Enter your name: ")
print(name.strip().replace(" ","").center(len(name.strip().replace(" ",""))+8,"*"))
