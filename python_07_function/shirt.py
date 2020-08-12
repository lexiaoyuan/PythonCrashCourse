def make_shirt(size, word):
    print("The size of this T-shirt is " + str(size))
    print("The word of this T-shirt is " + str(word))


make_shirt('XXL', 'Hello World!')


def make_shirt(size='XXXXL', word='I love Python'):
    print("The size of this T-shirt is " + str(size))
    print("The word of this T-shirt is " + str(word))


make_shirt()
make_shirt(size='M')
make_shirt(word='Life is short,you need Python')
