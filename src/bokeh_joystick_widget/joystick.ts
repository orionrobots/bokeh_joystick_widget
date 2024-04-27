import {InputWidget, InputWidgetView} from "models/widgets/input_widget"
import {div} from "core/dom"

declare var JoyStick: any // This declares that JoyStick is a global variable introduced by your external JS

export class JoystickView extends InputWidgetView {
  connect_signals(): void {
    super.connect_signals()
    // Connect signals here, for example, to listen for changes to model properties
  }

  render(): void {
    super.render()

    // Create a div element for the joystick and append it to the Bokeh layout
    const joyDiv = div({id: 'joyDiv', style: {width: '200px', height: '200px'}})
    this.el.appendChild(joyDiv)

    // Instantiate the JoyStick library on this div
    new JoyStick('joyDiv', {}, (stickData: any) => {
      // Update the Bokeh model with the joystick position
      this.model.x_value = stickData.xPosition
      this.model.y_value = stickData.yPosition
    })
  }
}

export class Joystick extends InputWidget {
  // This is where the "view" that Bokeh will use is defined
  default_view = JoystickView

  // You can define additional properties here, if needed
}
