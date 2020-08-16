filenames = ['cats.txt', 'dogs2.txt']
try:
    for filename in filenames:
        print(filename + ": ")
        with open(filename) as target:
            contents = target.read()
            print(contents)
except FileNotFoundError:
    # print("File not found !")
    pass
