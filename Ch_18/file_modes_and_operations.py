"""
    PYTHON FILE MODES   
        - Read ('r')
            * This is the default mode.
            * It opens a file so we can read data from it.
            * If the file does not exist, Python will raise a FileNotFoundError.
        - Write ('w')
            * This mode opens a file for writing text.
            * If the file already exists, it will overwrite the existing content.
            * If the file does not exist, it will create a new file.
        - Read & Write ('r+')
            * This mode opens a file for both reading and writing.
            * The file must exist, otherwise a FileNotFoundError will be raised.
            * The write() operation will overwrite the existing content from the beginning of the file.
        - Append ('a')
            * This mode opens a file for writing text.
            * Instead of overwriting the existing content, it adds new data to the end of the file.
            * If the file does not exist, it will create a new file.
        - Exclusive Create ('x')
            * This mode creates a new file and opens it for writing.
            * If a file with the same name already exists, it will raise a FileExistsError.
        - Read Binary ('rb')
            * This mode opens a file for reading data in binary format.
            * Instead of decoding the file into a text string, it returns raw bytes (e.g., b"data").
            * This is useful for reading non-text files like images, pdfs, or audio files.
        - Write Binary ('wb')
            * This mode opens a file for writing raw bytes.
            * It overwrites the existing content of the file or creates a new file if it doesn't exist.
            * It expects a byte object rather than text strings.
"""


# ============= Read Mode ('r') =============
file = open('file.txt', 'r', encoding='utf-8')        # reads an existing file
# file = open('file1.txt', 'r', encoding='utf-8')     # FileNotFoundError
data = file.read()
print(data)
file.close()
print('*'*40)


# ============= Write Mode ('w') =============
file = open('file.txt', 'w', encoding='utf-8')    # Overwrites to an existing file
file.write('Hello')
file.close()
file = open('file.txt', 'r', encoding='utf-8')
print(file.read())
file.close()

file = open('write.txt', 'w', encoding='utf-8')   # Create & Write
file.write('New File created through WRITE mode')
file.close()
file = open('write.txt', 'r', encoding='utf-8')
print(file.read())
file.close()
print('*'*40)


# ============= Append Mode ('a') =============
file = open('file.txt', 'a', encoding='utf-8')    # Appends to an existing file
file.write('\nNew data added through APPEND mode')
file.close()
file = open('file.txt', 'r', encoding='utf-8')
print(file.read())
file.close()
print('*'*40)


# ============= Exclusive Create Mode ('x') =============
file = open('exclusive.txt', 'x', encoding='utf-8')    # Creates a new file
file.write('File created through Exclusive Create mode.')
file.close()
file = open('exclusive.txt', 'r', encoding='utf-8')
print(file.read())
file.close()
print('*'*40)


# ============= Read Binary Mode ('rb') =============
# file = open('binary.txt', 'rb')    # FileNotFoundError
file = open('file.txt', 'rb')        # reads an existing file in binary format
print(file.read())
file.close()
print('*'*40)


# ============= Write Binary Mode ('wb') =============
file = open('byte.txt', 'wb')   # Creates new file
file.write(b'01001000')         # Writes raw bytes to the file
file.close()
file = open('byte.txt', 'rb')
print(file.read())
file.close()

file = open('file.txt', 'wb')   # Overwrites to an existing file
file.write(b'11111111')         # Writes raw bytes to the 
file.close()
file = open('file.txt', 'rb')
print(file.read())
file.close()
print('*'*40)  


# ============= Read & Write Mode ('r+') =============
with open('file.txt', 'r+', encoding='utf-8') as file:
    before = file.read()
    file.write('\nNew data added through r+ mode')
    file.seek(0)
    after = file.read()
print(f'Before writing:\n{before}\n')
print(f'After writing:\n{after}\n')
print('*'*40)