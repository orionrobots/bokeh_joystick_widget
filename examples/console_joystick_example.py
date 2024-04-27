from bokeh.document import Document
from bokeh.server.server import Server
from bokeh.application import Application
from bokeh.application.handlers.handler import Handler

from bokeh.plotting import figure

from bokeh.layouts import column
from bokeh.models import ColumnDataSource
from bokeh_joystick_widget import JoystickWidget


class ConsoleJoystick(Handler):
    def handle_move(self, event):
        print(f"move: {event.x}, {event.y}")

    def modify_document(self, doc: Document) -> None:
        # Make some dummy plot
        plot = figure(x_range=(-1,1), y_range=(-1,1), width=500, height=500)
        pl_x = [x*0.005 for x in range(2, 198)]
        pl_y = pl_x
        source = ColumnDataSource(data=dict(x=pl_x, y=pl_y))
        plot.line('x','y', source=source, line_width=3, line_alpha=0.6, color='#ed5565')

        joystick = JoystickWidget()
        # joystick on event
        # joystick.on_event(Moved, self.handle_move)
        doc.add_root(column(plot, joystick))

server = Server({'/': Application(ConsoleJoystick())}, port=5006)
server.start()
print("Server started at http://localhost:5006/")
server.run_until_shutdown()
