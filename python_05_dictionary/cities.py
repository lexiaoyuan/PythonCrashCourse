cities = {
    'daxin': {
        'country': 'china',
        'population': 300000,
        'fact': 'comfortable',
    },
    'dawu': {
        'country': 'china',
        'population': 600000,
        'fact': 'boring',
    },
    'wuhan': {
        'country': 'china',
        'population': 10000000,
        'fact': 'great'
    },
}

for city, infos in cities.items():
    print(city.title() + ":")
    for key, value in infos.items():
        print("\t" + key + ":" + str(value))
