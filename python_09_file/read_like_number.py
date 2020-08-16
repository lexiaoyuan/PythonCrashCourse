import json

filename = 'like_number.txt'

with open(filename) as f_obj:
    like_number = json.load(f_obj)
    print("I know your favorite number! It's " + like_number)
