import time
import pytest
from page_objects.checkout_page import CheckOutPage
from page_objects.order_women import OrderWomen


@pytest.fixture(scope='function')
def get_into_checkout_page(driver):
    page = OrderWomen(driver)
    page.add_top()

class TestCheckout:
    def test_checkout(self, driver, get_into_checkout_page):
        checkout = CheckOutPage(driver)
        checkout.fill_out_checkout()
        time.sleep(5)
        assert checkout.get_success_message() == "Thank you for your purchase!", "Unexpected error message"
