def describe_city(name, country='china'):
    print(name.title() + " is in " + country.title())


describe_city('dawu')
describe_city(name='daxin')
describe_city(name='wuhan', country='hubei')


def city_country(city, country):
    print(city.title() + ',' + country.title())


city_country('dawu', 'china')
city_country(country='china', city='daxin')
city_country(city='wuhan', country='china')
