'''
    - Define a function that:
        * takes a number and iterable (list or tuple containing numbers) as *args
        * returns the iterable with cube of each element of the iterable
        * if user didn't pass any args then print a message "Hey! you did not pass args" else return a list
    - Example:
        Input: to_power(3,*nums)    i.e. nums = [1,2,3]
        Output: [1,8,27]
'''


def to_power(num,*args):
    if args:
        return [n**num for n in args]
    else:
        return 'Hey! you did not pass args'

numbers = [1,2,3,4,5]
print(to_power(2,*numbers))
print(to_power(2))