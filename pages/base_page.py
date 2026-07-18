from playwright.sync_api import Page, expect
from utils.config import Config


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
        """Click the first visible locator matching `locator`.

        Use a wait to ensure the element is visible before clicking. This
        avoids Playwright's strict-mode errors when multiple elements match
        the selector and prevents flakiness in CI where elements may take
        longer to appear.
        """
        loc = self.page.locator(locator).first
        # Wait until visible with the configured timeout
        expect(loc).to_be_visible(timeout=Config.DEFAULT_TIMEOUT)
        loc.click()

    def fill(self, locator: str, text: str):
        """Fill the first visible input matching `locator`.

        Waits until visible to reduce flakiness on CI runners where elements
        may be present but not yet interactive.
        """
        loc = self.page.locator(locator).first
        expect(loc).to_be_visible(timeout=Config.DEFAULT_TIMEOUT)
        loc.fill(text)

    def get_text(self, locator: str) -> str:
        loc = self.page.locator(locator).first
        expect(loc).to_be_visible(timeout=Config.DEFAULT_TIMEOUT)
        return loc.inner_text()

    def is_visible(self, locator: str) -> bool:
        return self.page.locator(locator).is_visible()

    def wait_for_visible(self, locator: str, timeout: int = 10000):
        expect(self.page.locator(locator)).to_be_visible(timeout=timeout)

    def count(self, locator: str) -> int:
        return self.page.locator(locator).count()
