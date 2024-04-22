import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class OrderWomen(BasePage):
    __url = "https://magento.softwaretestingboard.com/"
    __women_button = (By.XPATH, "//span[text()='Women']")
    __top_link = (By.XPATH, "//a[text()='Tops']")
    __breathe_easy_tank = (By.CSS_SELECTOR, "img[alt='Breathe-Easy Tank']")
    __s_size = (By.CSS_SELECTOR, "#option-label-size-143-item-167")
    __color_pink = (By.CSS_SELECTOR, "#option-label-color-93-item-57")
    __color_white = (By.CSS_SELECTOR, "#option-label-color-93-item-59")
    __add_to_cart_button = (By.ID, "product-addtocart-button")
    __cart = (By.CSS_SELECTOR, ".action.showcart")
    __message = (By.XPATH, '//*[@role="alert"]/div/div')
    __proceed_to_checkout_button = (By.ID, "top-cart-btn-checkout")
    __update_cart_button = (By.ID, "product-updatecart-button")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def go_to_women(self):
        super()._open_url(self.__url)
        super()._click(self.__women_button)

    def add_top(self):
        super()._open_url(self.__url)
        super()._click(self.__women_button)
        super()._click(self.__top_link)
        super()._click(self.__breathe_easy_tank)
        super()._scroll_into_view(self.__add_to_cart_button)
        super()._click(self.__s_size)
        super()._click(self.__color_pink)
        super()._click(self.__add_to_cart_button)

    def select_white(self):
        super()._scroll_into_view(self.__color_white)
        super()._click(self.__color_white)
        super()._scroll_into_view(self.__update_cart_button)
        super()._click(self.__update_cart_button)



        #super()._wait_for_element_to_load(self.__message)
        #super()._scroll_into_view(self.__cart)
        #super()._click(self.__cart)
        #super()._click(self.__proceed_to_checkout_button)


