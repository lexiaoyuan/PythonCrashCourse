username = input("Please input your name:")
filename = 'guest.txt'
with open(filename, 'w') as target:
    target.write(username)
