"""
    - We have a file named 'file.txt' that contains following text:
        Saad, 1000
        Asad, 2000
        Akmal, 5000
        Usman, 9000
    - We have to read the file and write the content to another file named 'file2.txt' in followin format:
        Saad has 1000 points.
        Asad has 2000 points.
        Akmal has 5000 points.
        Usman has 9000 points.
"""


with (
    open('Ex_02.txt') as f1,
    open('solution.txt', 'a') as f2,
):
    for line in f1:
        name, points = line.split(',')
        f2.write(f'{name.strip()} has {points.strip()} points.\n')        