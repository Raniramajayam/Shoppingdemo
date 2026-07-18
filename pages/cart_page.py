from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ROWS = "#cart_info tbody tr"
    PRODUCT_NAME_CELL = "td.cart_description h4 a"
    PRODUCT_PRICE_CELL = "td.cart_price p"
    PRODUCT_QTY_CELL = "td.cart_quantity button"
    PRODUCT_TOTAL_CELL = "td.cart_total p"
    DELETE_BUTTON = "td.cart_delete a"
    # Prefer an explicit href for the checkout action to avoid ambiguous matches
    PROCEED_TO_CHECKOUT = "a[href='/checkout']"
    EMPTY_CART_MESSAGE = "#empty_cart"

    def get_item_count(self) -> int:
        return self.count(self.CART_ROWS)

    def get_product_names(self) -> list[str]:
        return self.page.locator(self.PRODUCT_NAME_CELL).all_inner_texts()

    def remove_item(self, index: int = 0):
        self.page.locator(self.DELETE_BUTTON).nth(index).click()

    def proceed_to_checkout(self):
        self.click(self.PROCEED_TO_CHECKOUT)

    def is_empty(self) -> bool:
        return self.is_visible(self.EMPTY_CART_MESSAGE)
