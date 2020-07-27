import matplotlib.pyplot as plt

plt.style.use("seaborn-darkgrid")

values = range(1, 5001)
squares = [x**3 for x in values]
fig, ax = plt.subplots()
ax.scatter(values, squares, c=values, cmap=plt.cm.Blues, s=10)
ax.axis([0, 5100, 0, 130000000000])

ax.set_title("Cube numbers", fontsize=24)
ax.set_xlabel("x - Value", fontsize=14)
ax.set_ylabel("y - Cube of value", fontsize=14)
ax.tick_params(axis="both", which="major", labelsize=14)
plt.savefig("scatter_cubes.png")
plt.show()