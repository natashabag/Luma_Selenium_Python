import time
import pytest
from page_objects.product_page import ProductPage
from page_objects.shopping_cart import ShoppingCart


@pytest.fixture(scope='function')
def get_to_checkout_page(driver):
    page = ProductPage(driver)
    page.open()
    page.go_to_women()
    page.view_product()
    page.add_top()


class TestCart:
    def test_delete(self, driver, get_to_checkout_page):
        cart_page = ShoppingCart(driver)
        cart_page.open()
        cart_page.delete_item()
        assert cart_page.empty_cart_get_message() == ("You have no items in your shopping cart.\nClick here to "
                                                      "continue shopping."), "Item was not deleted"

    def test_edit(self, driver, get_to_checkout_page):
        cart_page = ShoppingCart(driver)
        product_page = ProductPage(driver)
        cart_page.open()
        cart_page.edit_item()
        product_page.select_white()
        assert cart_page.define_color() == "White", "Unexpected error message"



