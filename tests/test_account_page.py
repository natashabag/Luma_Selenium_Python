import time

from page_objects import account_page
from page_objects.account_page import AccountPage
from page_objects.create_account_page import CreateAccountPage


class TestAccountPage:
    def test_creating_account(self, driver):
        create_account_page = CreateAccountPage(driver)
        create_account_page.create_account()
        customer_page = AccountPage(driver)
        assert customer_page.expected_url == customer_page.current_url, "Actual URL is not the same as expected"