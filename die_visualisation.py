from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die


die = Die()

results = [] #empty list

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

frequencies = []
for value in range(1, die.num_sides+1):
    frequncy = results.count(value)
    frequencies.append(frequncy)

x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title": "Result"}
y_axis_config = {"title": "Frequency of result"}
my_layout = Layout(title="Results of rolling one D6 1000 times",
                   xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({"data": data, "layout": my_layout}, filename="dr.html")