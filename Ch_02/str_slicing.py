''' 
    - String slicing means extracting a part (substring) of a string using indexes.
        * Syntax:  string[start : end : step]
        * It returns characters from 'start' index up to (not including) 'end' index.
'''

lang = "Python"
print(lang[0:2])
print("Saad"[1:3])

''' =========== Default Values =========== '''

# From start to end
print("Saad"[:3])

# From index to end
print("Saad"[1:])

# Full string
print("Saad"[:])

''' =========== Step Values =========== '''

# Skip characters
print("Saad"[::2])

# Reverse string
print("Saad"[::-1])
print("Saad"[-1::-1])   # same
    
# Negative Indexing in Slicing
print("Saad"[-3:-1])

# No error if range exceeds
print("Saad"[0:1000])


#   S = 0, -4       P = 0, -6
#   a = 1, -3       y = 1, -5
#   a = 2, -2       t = 2, -4
#   d = 3, -1       h = 3, -3
#                   o = 4, -2
#                   n = 5, -1