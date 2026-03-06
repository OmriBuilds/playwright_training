import pytest
from playwright.sync_api import sync_playwright
from python_training.NASA_Automation_Project.globals import URL


@pytest.fixture(scope="function")
def setup_playwright_nasa():
    print (f"starting playwright")
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(URL)
        yield page

        page.close()
        browser.close()
        print("####Test end###")