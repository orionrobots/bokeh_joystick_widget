import pexpect
import re
import time
import shutil

import pytest
from playwright.sync_api import sync_playwright, Page, expect


@pytest.fixture(scope="module")
def start_static_example():
    """Start the static example server."""
    # Start the static example server
    process = pexpect.spawn(
        "bokeh serve examples/static_joystick_example.py", encoding="utf-8"
    )
    time.sleep(2)
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()
            page.goto("http://localhost:5006/static_joystick_example")

            # Wait for the joystick widget to be visible
            expect(page.locator("#joyDiv")).to_be_visible(timeout=5000)

            yield (page, process)
        except AssertionError as e:
            # Look for errors in the JS console
            console_errors = page.evaluate("() => window.console.errors || []")
            if console_errors:
                print("JavaScript console errors:")
                for error in console_errors:
                    print(error)
            else:
                print("No JavaScript console errors found.")
            # Log the page content if the test fails
            print("Test failed, printing page content:")
            print(page.content())
            raise e
        finally:
            # Close the browser and process after tests
            browser.close()
            process.terminate()
            shutil.rmtree("bokeh-plot", ignore_errors=True)


@pytest.mark.usefixtures("start_static_example")
def test_joystick_widget_should_be_on_page(start_static_example):
    """Test that the joystick widget is present on the page."""
    page, process = start_static_example
    joystick_widget = page.locator("#joyDiv")
    expect(joystick_widget).to_be_visible()


def expect_exact_wrapper(process, pattern, timeout=0.5):
    """Wrapper for pexpect expect to handle TIMEOUT exceptions."""
    try:
        process.expect_exact(pattern, timeout=timeout)
    except pexpect.TIMEOUT:
        raise AssertionError(
            f"""Expected pattern '{pattern}' not found in output.
            Output: {process.before.strip()}"""
        )
    return process.before.strip()


@pytest.mark.usefixtures("start_static_example")
def test_moving_the_joystick_should_update_position(start_static_example):
    """Test that moving the joystick updates the position."""
    page, process = start_static_example
    print("Starting joystick movement test...")
    joystick_widget = page.locator("#joyDiv")
    # Determine the position of the joystick widget
    print("Finding joystick widget bounding box...")
    joystick_position = joystick_widget.bounding_box()
    if not joystick_position:
        pytest.fail("Joystick widget bounding box not found.")
    # Calculate the center of the joystick widget
    joystick_center_x = joystick_position["x"] + joystick_position["width"] / 2
    joystick_center_y = joystick_position["y"] + joystick_position["height"] / 2
    print(f"Joystick center position: ({joystick_center_x}, {joystick_center_y})")
    # Move the mouse to the center of the joystick widget
    print("Moving mouse to joystick center...")
    page.mouse.move(joystick_center_x, joystick_center_y)
    # Start a drag to simulate joystick movement to 50, 50 position
    page.mouse.down()
    print("Mouse down at joystick center, simulating joystick movement...")
    # Move the mouse to a new position (50, 50) relative to the joystick widget
    page.mouse.move(joystick_center_x + 50, joystick_center_y + 50)
    # Wait for a short duration to ensure the position is updated
    print("Mouse moved to (50, 50) relative to joystick center, checking output...")
    expect_exact_wrapper(
        process, "position changed: (0, 0) -> (100, -100)", timeout=0.5
    )

    # Release the mouse to stop dragging
    page.mouse.up()
    # It should go back to 0
    expect_exact_wrapper(
        process, "position changed: (100, -100) -> (0, 0)", timeout=0.5
    )
