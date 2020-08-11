flag = True
while flag:
    age = input("Your age is:")
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("free")
    elif age <= 12:
        print("10$")
    else:
        print("15$")
