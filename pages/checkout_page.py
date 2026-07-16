from pages.base_page import BasePage


class CheckoutPage(BasePage):
    ORDER_COMMENT_BOX = "textarea[name='message']"
    PLACE_ORDER_BUTTON = "a:has-text('Place Order')"
    ADDRESS_SECTION = "#address_delivery"
    REVIEW_ORDER_HEADER = "h2.heading:has-text('Review Your Order')"

    def add_order_comment(self, comment: str):
        self.fill(self.ORDER_COMMENT_BOX, comment)

    def place_order(self):
        self.click(self.PLACE_ORDER_BUTTON)

    def is_review_page_loaded(self) -> bool:
        return self.is_visible(self.REVIEW_ORDER_HEADER)
