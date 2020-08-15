while True:
    username = input("Please input your name:")
    if username == 'q':
        break
    print("Welcome " + username.title())
    filename = 'guest_book.txt'
    with open(filename, 'a') as target:
        target.write(username + "\n")
