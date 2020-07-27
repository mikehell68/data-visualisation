import matplotlib.pyplot as plt

plt.style.use("seaborn-darkgrid")

values = range(1, 1001)
squares = [x**2 for x in values]
fig, ax = plt.subplots()
ax.scatter(values, squares, c=values, cmap=plt.cm.Blues, s=10)
ax.axis([0, 1100, 0, 1100000])

ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("x - Value", fontsize=14)
ax.set_ylabel("y - Square of value", fontsize=14)
ax.tick_params(axis="both", which="major", labelsize=14)
plt.savefig("scatter_squares.png")
plt.show()