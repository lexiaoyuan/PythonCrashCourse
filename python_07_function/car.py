def make_car(manufacturer, size, **infos):
    car = {}
    car['制造商'] = manufacturer
    car['型号'] = size
    for key, value in infos.items():
        car[key] = value
    return car


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
