import matplotlib.pyplot as plt

plt.style.use("seaborn-darkgrid")

values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
ax.plot(values, squares, linewidth=3)

ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("x - Value", fontsize=14)
ax.set_ylabel("y - Square of value", fontsize=14)
ax.tick_params(axis="both", labelsize=14)
plt.show()