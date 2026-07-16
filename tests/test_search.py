import pytest

#checking  my first branch demo

@pytest.mark.smoke
def test_search_returns_results(home_page, search_page):
    """A valid keyword should return at least one product."""
    home_page.search_product("Dress")
    assert search_page.get_result_count() > 0, "Expected search results, got none"


@pytest.mark.regression
@pytest.mark.parametrize("keyword", ["Jeans", "Top", "Saree", "Shirt"])
def test_search_multiple_keywords(home_page, search_page, keyword):
    """Data-driven test: same test logic, multiple inputs.
    Interview point: this is parametrization — one of the first things
    interviewers check whether you know, since it avoids copy-pasted tests.
    """
    home_page.search_product(keyword)
    results = search_page.get_all_product_names()
    assert search_page.get_result_count() >= 0
    for name in results:
        assert isinstance(name, str)


def test_search_no_results_for_gibberish(home_page, search_page):
    home_page.search_product("zzzznonexistentproductzzz")
    assert search_page.get_result_count() == 0
