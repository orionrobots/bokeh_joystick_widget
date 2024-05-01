# Bokeh Joystick Widget

This is a custom widget for the Python Bokeh library that allows you to control a joystick via mouse drags or touch gestures.

The widget has x and y properties that are updated as the joystick is moved. The x and y properties are in the range -100 to 100.

The widget makes use of <https://github.com/bobboteck/JoyStick/>.

## Setup

## Usage


## Roadmap

- Get the example JS demo widget/bokeh model to work - whatever that widget is. - done
- Figure out how to get values back to the python end with it. - done
- Figure out how to swap their control for the joystick (however hacky)
    - Problem - the Ion slider is on a CDN. The Joystick repo is not. Can I load a local js file alongside that TS file?
        - It won't load with:

```python
  __javascript__ = [
      "joy.js"
  ]
```

        - Pasting the file onto the end of the typescript results in many Typescript compile errors - and is horrid hack.
        - Loading directly from github, not a CDN leads to a CORS error.
        - Loading from a local file with file:/// is not possible due to CORS and not suitable.
        - Loading from a local file with a webserver is not suitable for a library.
        - Ahh - jsdelivr.com is a CDN that can proxy github. That works.

- Figure out how to make that tidier.
- Figure out how to publish to PyPi (alpha) and test in a pip installed test.

