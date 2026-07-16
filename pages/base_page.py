from playwright.sync_api import Page, expect


class BasePage:
    """Parent class for every page object.

    Interview point: this is where the DRY principle lives. Instead of every
    page object re-implementing 'wait for element' / 'click safely' / 'get text',
    they inherit it once from here. If Playwright's API changes, you fix it
    in ONE file, not fifty.
    """

    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str):
        self.page.goto(url)

    def click(self, locator: str):
        self.page.locator(locator).click()

    def fill(self, locator: str, text: str):
        self.page.locator(locator).fill(text)

    def get_text(self, locator: str) -> str:
        return self.page.locator(locator).inner_text()

    def is_visible(self, locator: str) -> bool:
        return self.page.locator(locator).is_visible()

    def wait_for_visible(self, locator: str, timeout: int = 10000):
        expect(self.page.locator(locator)).to_be_visible(timeout=timeout)

    def count(self, locator: str) -> int:
        return self.page.locator(locator).count()
