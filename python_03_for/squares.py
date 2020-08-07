squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

print(min(squares))
print(max(squares))
print(sum(squares))

squares = [v**2 for v in range(1, 11)]
print(squares)
