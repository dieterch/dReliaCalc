from numpy import arange, linspace, pi, sin

from bokeh.models import LinearAxis, Range1d
from bokeh.plotting import figure, output_file, show

x = arange(-2*pi, 2*pi, 0.1)
y = sin(x)
y2 = linspace(0, 100, len(y))

output_file("twin_axis.html")

p = figure(
    x_range=(-6.5, 6.5),
    y_range=(-1.1, 1.1),
    plot_width=1000,
    plot_height=600,
    x_axis_label='Initial x-axis label',
    y_axis_label="Initial y-axis label",
)
p.yaxis.axis_label_text_color = 'red'

p.line(x, y, color="red")

p.extra_y_ranges = {"foo": Range1d(start=0, end=200)}
p.line(x, y2, color="blue", y_range_name="foo")
p.add_layout(LinearAxis(y_range_name="foo",
                        axis_label='test',
                        axis_label_text_color='blue'), 'left')

p.extra_y_ranges["foo2"] = Range1d(start=0, end=300)
p.line(x, y2, color="green", y_range_name="foo2")
p.add_layout(LinearAxis(y_range_name="foo2",
                        axis_label='test',
                        axis_label_text_color='green'), 'left')

show(p)
