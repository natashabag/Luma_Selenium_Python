import time

import pytest

from page_objects.account_page import AccountPage
from page_objects.product_page import ProductPage
from page_objects.sign_in_page import SignInPage
from tests.conftest import driver


@pytest.fixture(scope='function')
def sign_in(driver):
    sign__in_page = SignInPage(driver)
    sign__in_page.sign_in()


class TestProductPage:
    def test_product_to_cart(self, driver):
        order_women = ProductPage(driver)
        order_women.go_to_women()
        order_women.view_breathe_tank()
        order_women.add_top()
        assert order_women.check_if_success_message_displayed(), "Product is not added"

    def test_compare_two_products(self, driver):
        order_women = ProductPage(driver)
        order_women.go_to_women()
        order_women.view_breathe_tank()
        order_women.compare()
        order_women.go_to_women()
        order_women.view_antonia_tank()
        order_women.compare()
        time.sleep(3)
        order_women.go_to_compare()
        time.sleep(3)
        assert order_women.get_page_title() == "Compare Products", "Unexpected message"

    def test_search_field(self, driver):
        home_page = ProductPage(driver)
        home_page.open()
        home_page.search_for_product()
        product = home_page.get_product_to_search()
        assert home_page.get_page_title() == f"Search results for: '{product}'", "Unexpected error message"

    def test_add_product_to_wish_list(self, driver, sign_in):
        product_page = ProductPage(driver)
        product_page.open()
        product_page.go_to_women()
        product_page.view_breathe_tank()
        product_page.add_to_wish_list()
        assert product_page.get_page_title() == "My Wish List", "Wish List in not displayed"

    def test_remove_product_from_wish_list(self, driver, sign_in):
        product_page = ProductPage(driver)
        product_page.open()
        product_page.go_to_women()
        product_page.view_breathe_tank()
        product_page.add_to_wish_list()
        account_page = AccountPage(driver)
        account_page.delete_product_from_wish_list()
        assert product_page.get_page_title() == "My Wish List", "Wish List in not displayed"
