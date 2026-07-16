from pages.base_page import BasePage
from utils.config import Config


class HomePage(BasePage):
    # Locators — kept as class-level constants so they're easy to find/update
    PRODUCTS_LINK = "a[href='/products']"
    SEARCH_INPUT = "#search_product"
    SEARCH_BUTTON = "#submit_search"
    CART_LINK = "a:has-text('Cart')"
    SIGNUP_LOGIN_LINK = "a[href='/login']"
    LOGGED_IN_INDICATOR = "a:has-text('Logged in as')"

    def load(self):
        self.goto(Config.BASE_URL)
        return self

    def go_to_products(self):
        self.click(self.PRODUCTS_LINK)

    def search_product(self, keyword: str):
        self.click(self.PRODUCTS_LINK)
        self.fill(self.SEARCH_INPUT, keyword)
        self.click(self.SEARCH_BUTTON)

    def go_to_cart(self):
        self.click(self.CART_LINK)

    def is_loaded(self) -> bool:
        return "automationexercise" in self.page.url
