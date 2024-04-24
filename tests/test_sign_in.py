import time

from page_objects.account_page import AccountPage
from page_objects.sign_in_page import SignInPage


class TestSignIn:
    def test_signing_in(self, driver):
        sign_in_page = SignInPage(driver)
        sign_in_page.sign_in()
        customer_page = AccountPage(driver)
        time.sleep(3)
        assert customer_page.expected_url == customer_page.current_url, "Actual URL is not the same as expected"
