travel_places = ['beijing', 'chengdu', 'shanghai', 'xian', 'lasa']
print(travel_places)

print(sorted(travel_places))

print(travel_places)

print(sorted(travel_places, reverse=True))

print(travel_places)

travel_places.reverse()
print(travel_places)

travel_places.reverse()
print(travel_places)

travel_places.sort()
print(travel_places)

travel_places.sort(reverse=True)
print(travel_places)

print("I will travel to " + str(len(travel_places)) + " places")

somethings = ['taishan', 'huanghe', 'china', 'dawu', 'hanyu', 'coding']
print(somethings)
print("I want to climb " + somethings[0].title())
print("I like " + somethings[-1])

somethings[1] = 'changjiang'
print(somethings)

somethings.append('python')
print(somethings)

somethings.insert(2, 'huanghe')
print(somethings)

del somethings[-1]
print(somethings)

somethings.pop(1)
print(somethings)

somethings.remove('dawu')
print(somethings)

print(sorted(somethings))

somethings.sort()
print(somethings)

somethings.reverse()
print(somethings)

print(len(somethings))
