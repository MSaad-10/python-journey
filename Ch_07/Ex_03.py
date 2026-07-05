'''
    - Create a program that
        * takes a dictionary as input from user
        * inputs a list value for two keys
        * prints key-value pairs separately in output
'''


user_info = {}

name = input('Enter your name: ')
age = int(input("Enter your age: "))
fav_movies = input("Enter your fvrt movies (comma separated): ").split(',')
fav_songs = input("Enter your fvrt songs (comma separated): ").split(',')

user_info['name'] = name
user_info['age'] = age
user_info['fav_movies'] = fav_movies
user_info['fav_songs'] = fav_songs

for key, value in user_info.items():
    print(f'{key}: {value}')