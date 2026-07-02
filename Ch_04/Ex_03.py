'''
    - Create a function named 'is_palindrome' that:
        * takes one word in string as input
        * return TRUE if the string is palindrome
        * else return FALSE if not palindrome
'''


# Solution1
def is_palindrome(word):    
    if word == word[::-1]:
        return 'Palindrome'         
    return 'Not a Palindrome'

word = input('Enter a word: ')
print(is_palindrome(word))

# Solution2 - modified
def is_palindrome(word):
    return word == word[::-1]

word = input('Enter a word: ')
print(is_palindrome(word))