def city_functions(city, country, population=''):
    if population:
        formatted_city = city.title() + "," + country.title() + \
            " - population " + str(population)
    else:
        formatted_city = city.title() + "," + country.title()
    return formatted_city
