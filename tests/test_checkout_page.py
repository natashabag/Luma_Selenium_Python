import time
import pytest
from page_objects.checkout_page import CheckOutPage
from page_objects.product_page import ProductPage


@pytest.fixture(scope='function')
def get_to_checkout_page(driver):
    page = ProductPage(driver)
    page.open()
    page.go_to_women()
    page.view_product()
    page.add_top()


class TestCheckout:
    def test_checkout(self, driver, get_to_checkout_page):
        checkout = CheckOutPage(driver)
        checkout.fill_out_checkout()
        time.sleep(5)
        assert checkout.get_success_message() == "Thank you for your purchase!", "Unexpected error message"
