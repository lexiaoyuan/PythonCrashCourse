magicians = ['刘谦', '简纶廷', '郭皓炜']


def show_magicians(magicians):
    for magician in magicians:
        print(magician)


show_magicians(magicians)


def make_great(magicians):
    i = 0
    for magician in magicians:
        magician += ' the Great'
        magicians[i] = magician
        i = i+1


make_great(magicians)
show_magicians(magicians)


def make_great2(magicians):
    magicians2 = []
    for magician in magicians:
        magician += ' the Great'
        magicians2.append(magician)
    return magicians2


show_magicians(magicians)
show_magicians(make_great2(magicians))
show_magicians(magicians)
