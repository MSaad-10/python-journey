''' 
    - Strings are immutable in Python. 
    - One cannot change the original created string.
'''

lang = "python"
print(lang[0])
# lang[0] = 'P'   ❌

lang.replace('p','P')   
print(lang)   # no change
new_lang = lang.replace('p','P')
print(new_lang)   # changed