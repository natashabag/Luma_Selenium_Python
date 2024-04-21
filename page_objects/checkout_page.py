import time

from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage


class CheckOutPage(BasePage):
    fake = Faker('en_US')
    state = 'California'
    email = fake.email()
    first_name = fake.first_name()
    last_name = fake.last_name()
    street_address = fake.street_address()
    city = fake.city()
    zip_code = '92021'
    phone_number = fake.phone_number()

    __url = "https://magento.softwaretestingboard.com/checkout/#shipping"
    __email_field = (By.ID, "customer-email")
    __first_name_field = (By.NAME, "firstname")
    __last_name_field = (By.NAME, "lastname")
    __company_field = (By.NAME, "company")
    __street_address_field = (By.NAME, "street[0]")
    __city_field = (By.NAME, "city")
    __state_field = (By.NAME, "region_id")
    __phone_field = (By.NAME, "telephone")
    __zip_field = (By.NAME, "postcode")
    __fixed_rate_button = (By.NAME, "ko_unique_1")
    __next_button = (By.XPATH, "//div[@id='shipping-method-buttons-container']//button[@type='submit']")
    __place_order_button = (By.CSS_SELECTOR, "button[title='Place Order'] > span")


    def __init__(self, driver: WebDriver):
        super().__init__(driver)
    def open(self):
        super()._open_url(self.__url)

    def fill_out_checkout(self):
        super()._open_url(self.__url)
        super()._type(self.__email_field, self.email)
        super()._type(self.__first_name_field, self.first_name)
        super()._type(self.__last_name_field, self.last_name)
        super()._type(self.__company_field, "company")
        super()._type(self.__street_address_field, self.street_address)
        super()._scroll_into_view(self.__phone_field)
        super()._type(self.__city_field, self.city)
        super().select_option_from_dropdown(self.__state_field, "California")
        super()._type(self.__zip_field, self.zip_code)
        super()._type(self.__phone_field, self.phone_number)
        super()._scroll_into_view(self.__next_button)
        super()._click(self.__fixed_rate_button)
        super()._click(self.__next_button)
        super()._click(self.__place_order_button)








