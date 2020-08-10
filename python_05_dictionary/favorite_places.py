favorite_places = {
    'lexiaoyuan': ['gugong', 'changcheng', 'taishan'],
    'lexiaoyuanbeta': ['tiananmen', 'huashan'],
    'benjamin': ['dawu']
}
for name, favorite_place in favorite_places.items():
    print("The favorite places of " + name.title() + " are:")
    for place in favorite_place:
        print("\t" + place.title())
