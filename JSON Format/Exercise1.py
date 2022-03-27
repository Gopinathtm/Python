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
    inputname = input("Enter your name : ")
    if username == inputname:
        print(f"Welcome back, {username}")
    else:
        filename = 'username.json'
        with open(filename, 'w') as f:
            json.dump(inputname, f)
        print(f'We will remember you {inputname} ')


greet_user()

# output
""""
Enter your name : gopi
We will remember you gopi  
"""
