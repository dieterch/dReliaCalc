from bokeh.plotting import output_file, figure, show
from bokeh.models import LinearAxis, Range1d

x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]
y2 = [10, 9, 8, 7, 6]
y3 = [23, 24, 25, 26, 27]

output_file("twin_axis.html")

p = figure(x_range=(0, 6), y_range=(0, 6))

p.circle(x, y, color="red")

p.extra_y_ranges = {"foo1": Range1d(start=0, end=11)}
p.circle(x, y2, color="blue", y_range_name="foo1")
p.add_layout(LinearAxis(y_range_name="foo1"), 'left')

# CHANGES HERE: add to dict, don't replace entire dict
p.extra_y_ranges["foo2"] = Range1d(start=21, end=31)

p.circle(x, y3, color="green", y_range_name="foo2")
p.add_layout(LinearAxis(y_range_name="foo2"), 'right')

p.toolbar_location = "above"
show(p)
