from selenium.webdriver.remote.webdriver import WebDriver

class AccountPage:
    _url = "https://magento.softwaretestingboard.com/customer/account/"

    def __init__(self, driver: WebDriver):
        self._driver = driver

    @property
    def current_url(self) -> str:
        return self._driver.current_url

    @property
    def expected_url(self) -> str:
        return self._url
