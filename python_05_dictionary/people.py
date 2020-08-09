peoples = {
    'first_name': 'le',
    'last_name': 'xiaoyuan',
    'age': 21,
    'city': 'dawu'
}

print(peoples['first_name'])
print(peoples['last_name'])
print(peoples['age'])
print(peoples['city'])

for people in peoples.values():
    print(people)

lucky_number = {
    'lexiaoyuan': 6,
    'benjamin': 66,
    'lexiaoyuanbeta': 666,
    'yege': 6666,
    'ruanwei': 66666
}

print('lexiaoyuan'.title() + "'s lucky number is " +
      str(lucky_number['lexiaoyuan']))
print('benjamin'.title() + "'s lucky number is " +
      str(lucky_number['benjamin']))
print('lexiaoyuanbeta'.title() + "'s lucky number is " +
      str(lucky_number['lexiaoyuanbeta']))
print('yege'.title() + "'s lucky number is " +
      str(lucky_number['yege']))
print('ruanwei'.title() + "'s lucky number is " +
      str(lucky_number['ruanwei']))

for name, number in lucky_number.items():
    print(name.title() + "'s lucky number is " + str(number))

dictionary = {
    'if': 'if',
    'for': 'for',
    'list': 'list',
    'title': 'title',
    'upper': 'upper'
}

print("if: " + dictionary['if'])
print("for: " + dictionary['for'])
print("list: " + dictionary['list'])
print("title: " + dictionary['title'])
print("upper: " + dictionary['upper'])

for dic in dictionary.keys():
    print(dic)
