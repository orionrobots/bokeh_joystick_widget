from bokeh.models import InputWidget
from bokeh.core.properties import Bool, Float
from bokeh.util.compiler import TypeScript, JavaScript, bundle_models

class JoystickWidget(InputWidget):
    # __implementation__ = "joystick.ts"
    __implementation__ = [
            JavaScript("libs/JoyStick/joy.js"),
            TypeScript("joystick.ts"),
        ]

    # __javascript__ = ["joy.js"]
    auto_return_to_center = Bool(True)
    # Add properties that represent the joystick state
    x_value = Float(default=0)
    y_value = Float(default=0)
