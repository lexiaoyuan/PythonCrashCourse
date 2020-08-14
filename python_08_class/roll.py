from random import randint
x = randint(1, 6)


class Die():
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        x = randint(1, self.sides)
        print(x)


die6 = Die(6)
for i in range(10):
    die6.roll_die()
print('\n')

die10 = Die(10)
for i in range(10):
    die10.roll_die()
print('\n')

die20 = Die(20)
for i in range(10):
    die20.roll_die()
