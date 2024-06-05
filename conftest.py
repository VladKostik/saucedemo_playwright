import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="session")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def login_page(browser_context):
    page = browser_context.new_page()
    login_page = LoginPage(page)
    login_page.load()
    yield login_page
    page.close()


@pytest.fixture(scope="function")
def inventory_page(login_page):
    inventory_page = InventoryPage(login_page.page)
    yield inventory_page
