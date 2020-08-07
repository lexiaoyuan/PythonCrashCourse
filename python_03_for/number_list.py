for number in range(1, 21):
    print(number)

lists = list(range(1, 1000001))
# for list in lists:
# print(list)

print(min(lists))
print(max(lists))
print(sum(lists))

odd_list = list(range(1, 21, 2))
for odd in odd_list:
    print(odd)


three_list = list(range(3, 31, 3))
for three in three_list:
    print(three)

cube_list = []
for cube in range(1, 11):
    cube_list.append(cube**3)

for cube in cube_list:
    print(cube)

cube_list = [value**3 for value in range(1, 11)]
print(cube_list)
