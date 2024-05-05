from bokeh.models import InputWidget
from bokeh.core.properties import Bool, Float, Tuple, Nullable

class JoystickWidget(InputWidget):
    __implementation__ = "dist/bokeh_joystick_widget.js"

    # __view_module__ = "bokeh_joystick_widget"

    # __javascript__ = [
    #     # "https://cdn.jsdelivr.net/gh/bobboteck/JoyStick@v2.0.0/joy.js"
    #     "https://cdn.jsdelivr.net/gh/orionrobots/BobboTeckJoyStick@shadow-root-support/joy.js"
    # ]

    # Below are all the "properties" for this model. Bokeh properties are
    # class attributes that define the fields (and their types) that can be
    # communicated automatically between Python and the browser. Properties
    # also support type validation. More information about properties in
    # can be found here:
    #
    #    https://docs.bokeh.org/en/latest/docs/reference/core/properties.html#bokeh-core-properties

    auto_return_to_center = Bool(default=True, help="Return the joystick to center when released")
    # Add properties that represent the joystick state
    position = Tuple(Float, Float, default=[0,0], help="Position of the joystick")
