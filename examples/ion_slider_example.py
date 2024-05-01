from bokeh.io import show
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, CustomJS, Slider
from bokeh.plotting import figure

from bokeh.document import Document
from bokeh.server.server import Server
from bokeh.application import Application
from bokeh.application.handlers.handler import Handler


from double_ended_slider_widget import IonRangeSlider


class SliderApp(Handler):
    def range_changed(self, attr, old, new):
        print(f"range changed: {old} -> {new}")

    def modify_document(self, doc: Document) -> None:
        x = [x*0.005 for x in range(2, 198)]
        y = x
        source = ColumnDataSource(data=dict(x=x, y=y))
        plot = figure(width=400, height=400)
        plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6, color='#ed5565')

        callback_single = CustomJS(args=dict(source=source), code="""
            const f = cb_obj.value
            const x = source.data.x
            const y = Array.from(x, (x) => Math.pow(x, f))
            source.data = {x, y}
        """)

        slider = Slider(start=0, end=5, step=0.1, value=1, title="Bokeh Slider - Power")
        slider.js_on_change('value', callback_single)

        ion_range_slider = IonRangeSlider(start=0.01, end=0.99, step=0.01, range=(min(x), max(x)),
            title='Ion Range Slider - Range')

        ion_range_slider.on_change('range', self.range_changed)

        layout = column(plot, slider, ion_range_slider)
        doc.add_root(layout)


server = Server({'/': Application(SliderApp())}, port=5006)
server.start()
print("Server started at http://localhost:5006/")
server.run_until_shutdown()
