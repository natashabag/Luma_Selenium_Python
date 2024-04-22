from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage


class ShoppingCart(BasePage):
    __url = "https://magento.softwaretestingboard.com/checkout/cart/"
    __delete_button = (By.CSS_SELECTOR, ".cart.item a[title='Remove item']")
    __edit_button = (By.CSS_SELECTOR, "a[title='Edit item parameters']")
    __no_items_message = (By.CLASS_NAME, "cart-empty")
    __color_description = (By.XPATH, "/html//table[@id='shopping-cart-table']//td[@class='col item']//dd[2]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def delete_item(self):
        super()._scroll_into_view(self.__delete_button)
        super()._click(self.__delete_button)

    def empty_cart_get_message(self):
        return super()._get_text(self.__no_items_message, 10)

    def edit_item(self):
        super()._scroll_into_view(self.__edit_button)
        super()._click(self.__edit_button)

    def define_color(self):
        return super()._get_text(self.__color_description, 10)



