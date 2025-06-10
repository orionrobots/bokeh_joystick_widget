from subprocess import Popen
import re
import time
import shutil

import pytest
from playwright.sync_api import sync_playwright, Page, expect

@pytest.fixture(scope="module")
def start_static_example():
    """Start the static example server."""
    # Start the static example server
    process = Popen(["bokeh", "serve", "examples/static_joystick_example.py"])
    time.sleep(2)
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()
            page.goto("http://localhost:5006/static_joystick_example")

            # Wait for the joystick widget to be visible
            expect(page.locator("#joyDiv")).to_be_visible(timeout=5000)

            yield page
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
    page = start_static_example
    joystick_widget = page.locator("#joyDiv")
    expect(joystick_widget).to_be_visible()
