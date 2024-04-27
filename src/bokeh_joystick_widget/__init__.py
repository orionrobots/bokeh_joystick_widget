from bokeh.models import InputWidget
from bokeh.core.properties import Bool

class Joystick(InputWidget):
    __implementation__ = "joystick.ts"
    __javascript__ = ["https://github.com/bobboteck/JoyStick/raw/master/joy.min.js"]
    # TODO: Boolean for autoReturnToCenter - default is True
    auto_return_to_center = Bool(True)
