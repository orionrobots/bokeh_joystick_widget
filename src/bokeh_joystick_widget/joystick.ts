import * as p from "core/properties";
import { div } from "core/dom";
import { InputWidget, InputWidgetView } from "models/widgets/input_widget";


declare var JoyStick: any; // Assuming JoyStick is globally available

export class JoystickWidgetView extends InputWidgetView {
  declare model: JoystickWidget;

  connect_signals(): void {
    super.connect_signals();
    // Connect signals here, for example, to listen for changes to model properties
  }

  protected _render_input(): HTMLElement {
    const joyDiv = div({id: 'joyDiv', style: {width: '200px', height: '200px'}});
    this.el.appendChild(joyDiv);
    new JoyStick('joyDiv', {}, (stickData: any) => {
        this.model.x_value = stickData.xPosition;
        this.model.y_value = stickData.yPosition;
    });
    return joyDiv;
  }

  render(): void {
      super.render();
      this._render_input(); // Make sure to render the input
  }
}

export namespace JoystickWidget {
  export type Attrs = p.AttrsOf<Props>;

  export type Props = InputWidget.Props & {
    x_value: p.Property<number>;
    y_value: p.Property<number>;
    auto_return_to_center: p.Property<boolean>;
  };
}

export interface JoystickWidget extends JoystickWidget.Attrs {};

export class JoystickWidget extends InputWidget {
  declare properties: JoystickWidget.Props;
  declare __view_type__: JoystickWidgetView;

  constructor(attrs?: Partial<JoystickWidget.Attrs>) {
    super(attrs);
  }

  static {
    this.prototype.default_view = JoystickWidgetView;

    this.define<JoystickWidget.Props>(({Number, Boolean}) => ({
      x_value: [Number, 0],
      y_value: [Number, 0],
      auto_return_to_center: [Boolean, true]
    }));
  }
}
