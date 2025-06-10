from bokeh.plotting import figure, curdoc

from bokeh.layouts import column
from bokeh.models import ColumnDataSource
from bokeh_joystick_widget import JoystickWidget


# Make some dummy plot
plot = figure(x_range=(-1, 1), y_range=(-1, 1), width=500, height=500)
pl_x = [x * 0.005 for x in range(2, 198)]
pl_y = pl_x
source = ColumnDataSource(data=dict(x=pl_x, y=pl_y))
plot.line("x", "y", source=source, line_width=3, line_alpha=0.6, color="#ed5565")

joystick = JoystickWidget()
joystick.on_change('position', lambda attr, old, new: print(f"position changed: {old} -> {new}"))

curdoc().add_root(column(plot, joystick))
