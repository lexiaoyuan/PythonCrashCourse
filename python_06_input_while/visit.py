places = []
while True:
    place = input("If you could visit one place in the world,where would you go?")
    if place == 'quit':
        break
    places.append(place)

print("The holiday resorts that users dream of are:")
for place in places:
    print("\t" + place.title())
