import pytest


@pytest.mark.smoke
@pytest.mark.cart
def test_add_single_product_to_cart(home_page, search_page, cart_page):
    home_page.search_product("Dress")
    search_page.add_first_result_to_cart()
    home_page.go_to_cart()
    assert cart_page.get_item_count() == 1


@pytest.mark.regression
@pytest.mark.cart
def test_add_multiple_products_to_cart(home_page, search_page, cart_page):
    home_page.search_product("Top")
    search_page.add_nth_result_to_cart(0)
    home_page.load()  # back to home to search again
    home_page.search_product("Top")
    search_page.add_nth_result_to_cart(1)
    home_page.go_to_cart()
    assert cart_page.get_item_count() == 2


@pytest.mark.cart
def test_remove_item_from_cart(home_page, search_page, cart_page):
    home_page.search_product("Dress")
    search_page.add_first_result_to_cart()
    home_page.go_to_cart()
    assert cart_page.get_item_count() == 1

    cart_page.remove_item(0)
    assert cart_page.is_empty()
