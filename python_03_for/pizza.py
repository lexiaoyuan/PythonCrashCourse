pizzas = ['pork', 'beef', 'ham']
for pizza in pizzas:
    print("I like " + pizza + " pizza")

print("I really love pizza!")

animals = ['cat', 'dog', 'tigger', 'dragon']
for animal in animals:
    print("A " + animal + " would make a great pet")

print("Any of these animals would make a great pet!")

print("The first three items in the list are:")
print(animals[:3])

print("Two items from the middle of the list are:")
print(animals[1:-1])

print("The last three items in the list are:")
print(animals[-3:])

friend_pizzas = pizzas[:]

pizzas.append('chicken')
friend_pizzas.append('seafood')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
