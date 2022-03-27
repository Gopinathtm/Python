# simple program using json format to store and use data

import json


def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def greet_user():
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}")
    else:
        username = input('Enter your name : ')
        filename = 'username.json'
        with open(filename, 'w') as f:
            json.dump(username, f)
        print(f'We will remember you {username} ')


greet_user()

# output
""""
Enter your name : Gopinath
We will remember you Gopinath 
"""
