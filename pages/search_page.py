from pages.base_page import BasePage


class SearchPage(BasePage):
    SEARCHED_PRODUCTS_HEADER = "h2:has-text('Searched Products')"
    PRODUCT_CARDS = ".product-image-wrapper"
    PRODUCT_NAMES = ".productinfo p"
    ADD_TO_CART_BUTTONS = ".productinfo .add-to-cart"

    def get_result_count(self) -> int:
        return self.count(self.PRODUCT_CARDS)

    def get_all_product_names(self) -> list[str]:
        return self.page.locator(self.PRODUCT_NAMES).all_inner_texts()

    def add_first_result_to_cart(self):
        self.page.locator(self.ADD_TO_CART_BUTTONS).first.click()

    def add_nth_result_to_cart(self, index: int):
        self.page.locator(self.ADD_TO_CART_BUTTONS).nth(index).click()
