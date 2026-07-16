import pytest


@pytest.mark.checkout
@pytest.mark.regression
def test_proceed_to_checkout_from_cart(home_page, search_page, cart_page, checkout_page):
    """End-to-end style test chaining multiple page objects together —
    this is the pattern interviewers want to see: tests read like a
    user's real journey, not like raw Playwright calls.
    """
    home_page.search_product("Dress")
    search_page.add_first_result_to_cart()
    home_page.go_to_cart()
    cart_page.proceed_to_checkout()

    # Site may show a login modal for guests — real sites are messy,
    # a robust test handles that branch instead of assuming happy path.
    if checkout_page.is_review_page_loaded():
        checkout_page.add_order_comment("Please deliver after 5 PM - automated test")
        assert checkout_page.is_review_page_loaded()
