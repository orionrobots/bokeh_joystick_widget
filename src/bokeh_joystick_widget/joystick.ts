// The "core/properties" module has all the property types
import * as p from "core/properties"

// HTML construction and manipulation functions
import { input } from "core/dom"

// We will subclass in JavaScript from the same class that was subclassed
// from in Python
import { InputWidget, InputWidgetView } from "models/widgets/input_widget";


declare var JoyStick: any; // Assuming JoyStick is globally available

export class JoystickWidgetView extends InputWidgetView {
  declare model: JoystickWidget;
  theJoystick: any;
  input_el: HTMLElement;

  connect_signals(): void {
    super.connect_signals();
    // Connect signals here, for example, to listen for changes to model properties
  }

  protected _render_input(): HTMLElement {
    this.input_el = input({id: 'joyDiv', style: {width: '200px', height: '200px'}, type=})
    return this.input_el

  }

  render(): void {
      super.render()

      this.model.position = [0, 0]
      // this.theJoystick = new JoyStick(
      //   'joyDiv', {
      //     autoReturnToCenter: this.model.auto_return_to_center
      //   }, (stickData: any) => this.position_changed(stickData)
      // )
  }

  position_changed(stickData: any): void {
      // Do something when the position changes
      this.model.position = [stickData.xPosition, stickData.yPosition]
  }
}

export namespace JoystickWidget {
  export type Attrs = p.AttrsOf<Props>

  export type Props = InputWidget.Props & {
    position: p.Property<[number, number] | null>
    auto_return_to_center: p.Property<boolean>
  }
}

export interface JoystickWidget extends JoystickWidget.Attrs {};

export class JoystickWidget extends InputWidget {
  declare properties: JoystickWidget.Props;
  declare __view_type__: JoystickWidgetView;

  constructor(attrs?: Partial<JoystickWidget.Attrs>) {
    super(attrs)
  }

  static {
    this.prototype.default_view = JoystickWidgetView;

    this.define<JoystickWidget.Props>(({Tuple, Bool, Float, Nullable}) => ({
      position: [ Nullable(Tuple(Float, Float)), null ],
      auto_return_to_center: [Bool, true]
    }))
  }
}
