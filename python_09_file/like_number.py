import json

filename = 'like_number.txt'

try:
    with open(filename) as f_obj:
        like_number = json.load(f_obj)
    print("I know your favorite number! It's " + like_number)
except FileNotFoundError:
    like_number = input("What's your favorite number ")
    with open(filename, 'w') as f_obj:
        json.dump(like_number, f_obj)
