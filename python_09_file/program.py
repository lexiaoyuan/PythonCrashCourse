while True:
    program = input("Why do you like programming?")
    if program == 'q':
        break
    filename = 'reason.txt'
    with open(filename, 'a') as target:
        target.write(program + "\n")
