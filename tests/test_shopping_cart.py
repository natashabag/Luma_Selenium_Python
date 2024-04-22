import time
import pytest
from page_objects.order_women import OrderWomen
from page_objects.shopping_cart import ShoppingCart


@pytest.fixture(scope='function')
def get_into_checkout_page(driver):
    page = OrderWomen(driver)
    page.add_top()


class TestCart:
    def test_delete(self, driver, get_into_checkout_page):
        cart_page = ShoppingCart(driver)
        cart_page.open()
        cart_page.delete_item()
        assert cart_page.empty_cart_get_message() == ("You have no items in your shopping cart.\nClick here to "
                                                      "continue shopping."), "Item was not deleted"
    def test_edit(self, driver, get_into_checkout_page):
        cart_page = ShoppingCart(driver)
        product_page = OrderWomen(driver)
        cart_page.open()
        cart_page.edit_item()
        product_page.select_white()
        assert cart_page.define_color() == "White", "Unexpected error message"


