'''
    - Create a function that:
        * takes multiple inputs through *args and return the sum of integer and float values.
        * if the *args contain string, list or any other data type value then the function should return an error message. 
'''


def valid_sum(*args):
    if all((type(arg) == int or type(arg) == float) for arg in args):
        return sum(args)
    else:
        return "Invalid Input"
    
print(valid_sum(1,2,3,4,5,6,9.8))
print(valid_sum(1,2,3,4,5,6,"string",('tuple')))