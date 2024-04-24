from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class AccountPage(BasePage):
    _url = "https://magento.softwaretestingboard.com/customer/account/"

    # valid credentials:
    __username = "annsmithtest@testmail.com"
    __password = "MyPassword123!"

    def __init__(self, driver: WebDriver):
        self._driver = driver

    @property
    def current_url(self) -> str:
        return self._driver.current_url

    @property
    def expected_url(self) -> str:
        return self._url
