from faker import Faker
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class CreateAccountPage(BasePage):
    __url = "https://magento.softwaretestingboard.com/customer/account/create/"
    # customer credentials:
    fake = Faker('en_US')
    __email = fake.email()
    __first_name = fake.first_name()
    __last_name = fake.last_name()
    __password = "MyPassword123!"

    # fields:
    __first_name_field = (By.ID, "firstname")
    __last_name_field = (By.ID, "lastname")
    __email_field = (By.ID, "email_address")
    __password_field = (By.ID, "password")
    __confirm_password_field = (By.ID, "password-confirmation")
    __create_account_button = (By.CSS_SELECTOR, "button[title = 'Create an Account'] > span")

    # creating an account:
    def create_account(self):
        super()._open_url(self.__url)
        super()._type(self.__first_name_field, self.__first_name)
        super()._scroll_into_view(self.__create_account_button)
        super()._type(self.__last_name_field, self.__last_name)
        super()._type(self.__email_field, self.__email)
        super()._type(self.__password_field, self.__password)
        super()._type(self.__confirm_password_field, self.__password)
        super()._click(self.__create_account_button)




