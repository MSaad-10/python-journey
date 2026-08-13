"""
    Python 'os' Module
        - The os module is Python's built-in module for interacting with the operating system.
        - In simple words, os lets your Python program communicate with your computer's operating system.
        - You can use it to:
            * Work with files and folders
            * Get the current working directory
            * Create/delete directories
            * Rename files
            * Check whether files exist
            * Get environment variables
            * Work with file paths
"""

# ============= Importing the os Module =============
import os


# ============= os.getcwd() =============
''' Returns the current working directory. '''
print(os.getcwd())
print('-'*40)


# ============= os.listdir() =============
''' Returns a list of all files and folders in the specified directory.'''
print(os.listdir(), '\n')

# You can also specify a path to list files and folders in a different directory.
print(os.listdir(r'C:\Users\hp\Documents'))
print('-'*40)


# ============= os.mkdir() =============
''' Creates a new directory with the specified name. '''
os.mkdir('projects')
print(os.listdir())
print('-'*40)


# ============= os.makedirs() =============
''' Creates nested directories. '''
os.makedirs('projects/python/os_module')
print(os.listdir('projects/python'))
print('-'*40)


# ============= os.rmdir() =============
''' Removes an empty directory. '''
os.rmdir('projects/python/os_module')
print(os.listdir('projects/python'))
print('-'*40)


# ============= open(filename, mode) =============
''' Creates a new file or opens an existing file. '''
open('file.txt', 'w').close()


# ============= os.remove() =============
''' Deletes a file. '''
os.remove('file.txt')


# ============= os.rename() =============
''' Renames a file or folder. '''
os.rename('os_module.py', 'module.py')
os.mkdir('new_folder')
os.rename('new_folder', 'renamed_folder')


# ============= Checking Whether a File Exists =============
''' Checks whether a file or folder exists. '''
print(os.path.exists('module.py'))
print(os.path.exists('renamed_folder'))

# Real-World Example
if os.path.exists('module.py'):
    print('File exists.')
else:
    open('module.py', 'w').close()


# ============= os.path.isfile() =============
''' Checks whether a path is a file. '''
open('module.py', 'w').close()
print(os.path.isfile('module.py'))
print(os.path.isfile('renamed_folder'))
print('-'*40)


# ============= os.path.isdir() =============
''' Checks whether a path is a directory. '''
print(os.path.isdir('module.py'))
os.mkdir('renamed_folder')
print(os.path.isdir('renamed_folder'))
print('-'*40)


# ============= os.path.getsize() =============
''' Returns the size of a file in bytes. '''
print(os.path.getsize('os_module.py'))
print('-'*40)


# ============= os.path.abspath() =============
''' Returns the absolute path of a file or folder. '''
print(os.path.abspath('os_module.py'))  
print('-'*40)


# ============= os.path.join() =============
''' Joins one or more path components intelligently. '''
path = os.path.join('projects', 'python', 'os_module.py')
print(path)
print('-'*40)


# ============= os.path.basename() =============
''' Returns the base name of a file or folder. '''
path = os.path.abspath('os_module.py')
print(os.path.basename(path))
print('-'*40)


# ============= os.path.dirname() =============
''' Returns the directory name of a file or folder. '''
path = os.path.abspath('os_module.py')
print(os.path.dirname(path))
print('-'*40)


# ============= os.environ =============
''' Returns a dictionary containing the user's environment variables. '''
print(os.environ)

# More commonly:
print(os.environ.get("API_KEY"))  # Get the value of an environment variable
print('-'*40)


# ============= os.system() =============
''' Executes a command in the system shell. '''
os.system('dir')
os.system('echo Hello World')
print('-'*40)


# ============= os.walk() =============
''' Generates the file names in a directory tree by walking the tree either top-down or bottom-up. '''
for root, dirs, files in os.walk('../../python'):
    print('Root:', root)
    print('Directories:', dirs)
    print('Files:', files)
    print('-'*40)


# ============= os.path.splitext() =============
''' Splits the file name into a tuple containing the file name and its extension. '''
file_name = 'example.txt'
name, extension = os.path.splitext(file_name)
print(f'Name:     \t{name}')
print(f'Extension:\t{extension}')
print('-'*40)


# ============= os.chdir() =============
''' Changes the current working directory. '''
os.chdir('..')
print(os.getcwd())
print('-'*40)


# ============= Import 'time' module =============
import time


#============= os.path.getmtime() =============
''' Returns the last modification time of a file. '''
print(time.ctime(os.path.getmtime('os_module.py')))
print('-'*40)


# ============ os.path.getatime() =============
''' Returns the last access time of a file. '''
print(time.ctime(os.path.getatime('os_module.py')))
print('-'*40)


# ============ os.path.getctime() =============
''' Returns the creation time of a file. '''
print(time.ctime(os.path.getctime('os_module.py')))
print('-'*40)


# ============ os.path.isabs() =============
''' Checks whether a path is an absolute path. '''
print(os.path.isabs('os_module.py'))
print('-'*40)


# ============ shutil.rmtree() =============
''' Deletes a directory and all its contents. '''
import shutil
os.makedirs('new_folder/sub_folder')
shutil.rmtree('new_folder')