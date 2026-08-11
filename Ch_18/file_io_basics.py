"""
    File I/O in Python
        - I/O means:
            * Input → Getting data into your program
            * Output → Sending data somewhere
"""


# ============= Opening a File — open(filename, mode) =============
''' Before working with a file, you need to open it. '''
file = open('file.txt', 'r', encoding='utf-8')
file.close()


# ============= Read a File — read() =============
''' The read() method reads the entire file and returns it as a string. '''
file = open('file.txt', 'r', encoding='utf-8')
file_data = file.read()
print(file_data, '\n')
file.close()

''' You can also specify the number of characters to read from the file. '''
file = open('file.txt', 'r', encoding='utf-8')
file_data = file.read(15)    # reads first 15 characters
print(file_data)
file.close() 
print('*'*40)


# ============= tell() Method =============
''' The tell() method returns the current position of the file cursor in the file. '''
file = open('file.txt', 'r', encoding='utf-8')
print(f'Position before file reading:\t{file.tell()}')
data = file.read()
print(f'Position after file reading:\t{file.tell()}')
file.close()
print('*'*40)


# ============= seek() Method =============
''' The seek() method changes the position of the file cursor in the file. '''
file = open('file.txt', 'r', encoding='utf-8')
print(f'Current Position of the file cursor:     \t{file.tell()}')
file.seek(10)    
print(f'Position of the file cursor after seek():\t{file.tell()} \n')
data = file.read()
print(data)         # Because we moved the cursor to the 10th position.
file.close()
print('*'*40)


# ============= readline() Method =============
''' The readline() method reads a single line from the file. '''
file = open('file.txt', 'r', encoding='utf-8')
print(file.readline(), end='')    # reads the first line    
print(file.readline(), end='')    # reads the second line
file.close()
print('*'*40)


# ============= Reading Lines One by One =============
# while loop
file = open('file.txt', 'r', encoding='utf-8')
line = file.readline()    
while line:
    print(line, end='')    
    line = file.readline()
print()
print()
file.close()

# for loop
file = open('file.txt', 'r', encoding='utf-8')
for line in file.readlines():
    print(line, end='')
file.close()
print()
print('*'*40)


# ============= readlines() Method =============
''' The readlines() method reads all the lines of a file and returns them as a list of strings. '''
file = open('file.txt', 'r', encoding='utf-8')
lines = file.readlines()
print(lines)
file.close()
print('*'*40)


# ============= A Very Important Behavior of read() =============
file = open('file.txt', 'r', encoding='utf-8')
print(f'Current position: {file.tell()} \n')
print(file.read())    # reads the entire file
print()
print(f'Position after read: {file.tell()}')
print(file.read())    # reads nothing because the cursor is at the end of the file
file.close()
print('*'*40)


# ============= Opening File by its Path =============
file = open(r'D:\Code\python-journey\Ch_17\file.txt', 'r', encoding='utf-8')    # Use 'r' to treat the string as a raw string, so that backslashes are not treated as escape characters.
content = file.read()
print(content)
file.close()
print('*'*40)