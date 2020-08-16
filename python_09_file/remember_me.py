import json

""" username = input("What is your name?")

filename = 'username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We'll remember ou when you come back, " + username + "!") """

""" # 如果以前存储了用户名，就加载它
# 否则，就提示用户输入用户名并存储它
filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!") """


""" def greet_user():
    # 问候用户，并指出其名字
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, " + username + "!")
    else:
        print("Welcome back, " + username + "!")


greet_user() """


def get_store_username():
    """ 如果存储了用户名，就获取它 """
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """ 提示用户输入用户名 """
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """ 问候用户，并指出其名字 """
    username = get_store_username()
    if username:
        y_or_n = input(username + " is you? y/n ")
        if y_or_n == 'y':
            print("Welcome back, " + username + "!")
        if y_or_n == 'n':
            username = get_new_username()
            print("We'll remember you when you come back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")


greet_user()
