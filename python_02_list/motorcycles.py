motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('feige')
print(motorcycles)

motorcycles.insert(2, 'yongjiu')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

second_owned = motorcycles.pop(2)
print(second_owned)

print(motorcycles)

motorcycles.remove('yamaha')
print(motorcycles)
