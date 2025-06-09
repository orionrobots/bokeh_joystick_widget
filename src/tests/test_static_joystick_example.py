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
    process = Popen(["python", "examples/static_joystick_example.py"])
    time.sleep(2)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto("http://localhost:5006/static_joystick_example.html")

        # Wait for the joystick widget to be visible
        expect(page.locator(".bk-joystick-widget")).to_be_visible(timeout=5000)

        yield page

        # Close the browser and process after tests
        browser.close()
        process.terminate()
        shutil.rmtree("bokeh-plot", ignore_errors=True)
