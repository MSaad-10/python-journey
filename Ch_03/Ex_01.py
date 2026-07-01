'''
    NUMBER GUESSING GAME
    - Make a variable like 'win_num' and assign a random numnber to it.
    - Ask user to guess the number.
    - If user guessed correctly then print "YOU WIN!!"
    - if user do not guessed correctly then:
        * guessed lower than actual num: "too low"
        * guessed higher than actual num: "too high"

    Use random library to generate random numbers
'''


# Solution1
import random
win_num = random.randint(0,10)
flag = True
while flag:
    guess_num = int(input("Guess original num (0-10): "))
    if guess_num == win_num:
        print("YOU WON!!")
        flag = False
    else:
        if guess_num < win_num:
            print("too low")
        else:
            print("too high")


# Solution2 - modified version
import random
real_num = random.randint(0, 100)
count = 1
flag = True
guess_num = int(input("Guess the number (0-100): ")) 
while flag:
    if guess_num != real_num:
        if guess_num < real_num:
            print("Too low!!")
        else:
            print("Too high!!")
        count += 1
        guess_num = int(input("Guess again: "))
    else:
        print("YOU WIN!!")
        print(f"You guessed this number in {count} times")
        flag = False