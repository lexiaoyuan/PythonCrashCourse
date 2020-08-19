import pygal
from die import Die

# 创建一个D6
# die = Die()

# 创建两个D6骰子
# die_1 = Die()
# die_2 = Die()

# 创建一个D6和一个D10
die_1 = Die()
die_2 = Die(10)

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    # result = die.roll()
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
# for value in range(1, die.num_sides+1):
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()

# hist.title = "Results of rolling one D6 1000 times."
# hist.x_labels = ['1', '2', '3', '4', '5', '6']
# hist.title = "Results of rolling two D6 dice 1000 times."
# hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.title = "Results of rolling a D6 and a D10 1000 times."
# hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
#                  '11', '12', '13', '14', '15', '16']
hist.x_labels = die_1.auto_labels(2, 16)
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

# hist.add('D6', frequencies)
# hist.add('D6 + D6', frequencies)
hist.add('D6 + D10', frequencies)
# hist.render_to_file('die.visual.svg')
# hist.render_to_file('die.visual2.svg')
hist.render_to_file('die.visual3.svg')

# print(results)
print(frequencies)
