'''
    EXERCISE: WATCH COCO
        - Ask user's name and age
        - If user's name start with ('a' or 'A') and age is above 10 then:
            - Print 'you can watch coco movie'
            - Else print 'sorry, you cannot watch coco'
'''

name, age = input("Enter your name & age (space separated): ").split()
age = int(age)
if name.startswith('a' or 'A') and age > 10:
    print("You can watch coco movie")
else:
    print("Sorry, You cannot watch coco")