''' 
        "She is beautiful and she is a good dancer"
    - Find position of second 'is' by using position of first 'is'
'''

text = "She is beautiful and she is a good dancer"
is_pos1 = text.find('is')
is_pos2 = text.find('is',is_pos1+1)
print(is_pos2)