import matplotlib.pyplot as plt

x_values = list(range(1, 6))
y_values = [x**3 for x in x_values]

plt.plot(x_values, y_values)

plt.title("Cube of value")
plt.xlabel("Value")
plt.ylabel("Cube of value")

plt.show()

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=20)
plt.axis([0, 5001, 0, 125000001])
plt.show()
