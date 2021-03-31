from bokeh.io import push_notebook, show, output_notebook
from bokeh.plotting import figure, output_file, show
from bokeh.models import LinearAxis, Range1d

import dmyplant2
import arrow

import pandas as pd
import numpy as np

import sys
import warnings
warnings.simplefilter(action='ignore', category=pd.errors.PerformanceWarning)


dmyplant2.cred()
mp = dmyplant2.MyPlant(0)
#dval = dmyplant2.Validation.load_def_csv("input.csv")
#vl = dmyplant2.Validation(mp, dval, cui_log=False)

e = dmyplant2.Engine_SN(mp, 1225799)
print(f"{e} {e.id}")

dat = {
    161: ['CountOph', 'h'],
    102: ['PowerAct', 'kW'],
    107: ['Various_Values_SpeedAct', '1/min'],
    217: ['Hyd_PressCrankCase', 'mbar'],
    16546: ['Hyd_PressOilDif', 'bar']
}

df = e._batch_hist_dataItems(
    itemIds=dat,
    p_from=arrow.get('2021-03-05 04:00').to('Europe/Vienna'),
    p_to=arrow.get('2021-03-05 07:00').to('Europe/Vienna'),
    timeCycle=30)

df['PartsOph'] = df.CountOph - e.oph_start

output_file("twin_axis.html")
# output_notebook()

df = df.set_index(['datetime'])
df.loc['2021-03-05 05:00':'2021-03-05 06:00']

p = figure(
    #x_range=(-6.5, 6.5),
    y_range=(0, 5000),
    plot_width=1200,
    plot_height=800,
    x_axis_label='datetime',
    y_axis_label="PowerAct",
    x_axis_type='datetime'
)
p.yaxis.axis_label_text_color = 'red'

#p.line(x, y, color="red")
p.line(source=df, x='datetime', y='PowerAct', color="red")

p.extra_y_ranges = {"foo": Range1d(start=0, end=1800)}
#p.line(x, y2, color="blue", y_range_name="foo")
p.line(source=df, x='datetime', y='Various_Values_SpeedAct',
       color="blue", y_range_name="foo")
p.add_layout(LinearAxis(y_range_name="foo",
                        axis_label='SpeedAct',
                        axis_label_text_color='blue'), 'right')

p.extra_y_ranges["foo2"] = Range1d(start=-100, end=100)
#p.line(x, y2, color="green", y_range_name="foo2")
p.line(source=df, x='datetime', y='Hyd_PressCrankCase',
       color="green", y_range_name="foo2")
p.add_layout(LinearAxis(y_range_name="foo2",
                        axis_label='Hyd_PressCrankCase',
                        axis_label_text_color='green'), 'right')


p.extra_y_ranges["foo3"] = Range1d(start=0, end=1)
p.line(source=df, x='datetime', y='Hyd_PressOilDif',
       color="orange", y_range_name="foo3")
p.add_layout(LinearAxis(y_range_name="foo3",
                        axis_label='Hyd_PressOilDif',
                        axis_label_text_color='orange'), 'right')

show(p)
