from random import randint


class Die():
    """ 表示一个骰子的类 """

    def __init__(self, num_sides=6):
        """ 骰子默认为6面 """
        self.num_sides = num_sides

    def roll(self):
        """ 返回一个位于1和骰子面数之间的随机值 """
        return randint(1, self.num_sides)

    def auto_labels(self, start, end):
        # labels = []
        # for value in range(start, end+1):
        #     labels.append(str(value))
        labels = [str(value) for value in range(start, end+1)]
        # print(labels)
        return labels
