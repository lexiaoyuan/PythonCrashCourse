class Employee():
    def __init__(self, last, first, money):
        self.last = last
        self.first = first
        self.money = money

    def give_raise(self, raises=5000):
        self.raises = raises
        return raises
