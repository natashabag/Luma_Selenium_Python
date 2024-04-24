from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage


class SignInPage(BasePage):
    __url = "https://magento.softwaretestingboard.com/customer/account/login"

    # valid credentials:
    __email = "annsmithtest@testmail.com"
    __password = "MyPassword123!"

    # fields:
    __email_field = (By.ID, "email")
    __password_field = (By.ID, "pass")

    # buttons:
    __sign_in_button = (By.ID, "send2")

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def sign_in(self):
        super()._open_url(self.__url)
        super()._scroll_into_view(self.__sign_in_button)
        super()._type(self.__email_field, self.__email)
        super()._type(self.__password_field, self.__password)
        super()._click(self.__sign_in_button)

