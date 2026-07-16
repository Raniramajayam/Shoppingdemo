import pytest
from playwright.sync_api import sync_playwright

from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.config import Config
from utils.logger import get_logger

log = get_logger(__name__)


@pytest.fixture(scope="session")
def playwright_instance():
    """One Playwright process for the whole test run."""
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_instance):
    """One browser instance shared across the session — launching a browser
    is expensive, so we don't do it per-test.
    """
    browser = playwright_instance.chromium.launch(headless=Config.HEADLESS)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def context(browser):
    """A FRESH browser context per test = isolated cookies/storage/cache.
    This is the key trick for test independence: tests never leak
    login state or cart state into each other.
    """
    context = browser.new_context(viewport={"width": 1440, "height": 900})
    context.set_default_timeout(Config.DEFAULT_TIMEOUT)
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()


@pytest.fixture(scope="function")
def home_page(page):
    home = HomePage(page)
    home.load()
    return home


@pytest.fixture(scope="function")
def search_page(page):
    return SearchPage(page)


@pytest.fixture(scope="function")
def cart_page(page):
    return CartPage(page)


@pytest.fixture(scope="function")
def checkout_page(page):
    return CheckoutPage(page)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Auto-capture a screenshot on failure, attached to the HTML report.
    This is the thing every interviewer asks about: 'how do you debug
    a failure you can't reproduce locally?' Answer: this hook.
    """
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            screenshot_path = f"reports/failure_{item.name}.png"
            page.screenshot(path=screenshot_path)
            log.info(f"Screenshot saved: {screenshot_path}")
