import time

import pytest

from page_objects.product_page import ProductPage
from page_objects.sign_in_page import SignInPage
from tests.conftest import driver

@pytest.fixture(scope='function')
def sign_in(driver):
    sign__in_page = SignInPage(driver)
    sign__in_page.sign_in()
class TestOrderWomen:
    def test_order(self, driver):
        order_women = ProductPage(driver)
        order_women.go_to_women()
        order_women.view_product()
        order_women.add_top()
        assert order_women.check_if_success_message_displayed(), "Product is not added"

        time.sleep(10)

    def test_compare(self, driver):
        order_women = ProductPage(driver)
        order_women.go_to_women()
        order_women.view_product()
        order_women.compare()
        order_women.go_to_women()
        order_women.view_product2()
        order_women.compare()
        time.sleep(3)
        order_women.go_to_compare()
        time.sleep(3)
        assert order_women.get_page_title() == "Compare Products", "Unexpected message"

    def test_search(self, driver):
        home_page = ProductPage(driver)
        home_page.open()
        home_page.search_for_product()
        product = home_page.get_product()
        assert home_page.get_page_title() == f"Search results for: '{product}'", "Unexpected error message"

    def test_adding_product_to_wish_list(self, driver, sign_in):
        product_page = ProductPage(driver)
        product_page.open()
        product_page.go_to_women()
        product_page.view_product()
        product_page.add_to_wish_list()
        assert product_page.get_page_title() == "My Wish List", "Wish List in not displayed"


    def test_leave_review(self, driver):
        product_page = ProductPage(driver)
        product_page.go_to_women()
        product_page.view_product()
        product_page.leave_review()
        time.sleep(3)


