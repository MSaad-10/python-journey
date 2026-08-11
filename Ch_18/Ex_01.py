"""
    - Take two files file1.txt and file2.txt.
    - Write a program that reads the content of file1.txt and writes it to file2.txt.
    - If file2.txt does not exist, create it.
"""


try:
    with (
        open('Ex_01.txt', 'r', encoding='utf-8') as file1,
        open('file2.txt', 'w', encoding='utf-8') as file2
    ):
        file2.write(file1.read())
        print("File copied successfully.")
except FileNotFoundError:
    print("Error: file1.txt not found.")
except PermissionError:
    print("Error: Permission denied.")
except Exception as e:
    print(f"An error occurred: {e}")