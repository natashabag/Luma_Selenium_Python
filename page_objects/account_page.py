from faker import Faker
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class AccountPage(BasePage):
    __url = "https://magento.softwaretestingboard.com/customer/account/create/"
    # customer credentials:
    fake = Faker('en_US')
    email = fake.email()
    first_name = fake.first_name()
    last_name = fake.last_name()
    password = "MyPassword123!"

    # fields:
    __first_name_field = (By.ID, "firstname")
    __last_name_field = (By.ID, "lastname")
    __email_field = (By.ID, "email_address")
    __password_field = (By.ID, "password")
    __confirm_password_field = (By.ID, "password-confirmation")
    __create_account_button = ()

    def create_account(self):
        super()._open_url(self.__url)
        super()._type(self.__email_field, self.email)
        super()._type(self.__first_name_field, self.first_name)
        super()._type(self.__last_name_field, self.last_name)



