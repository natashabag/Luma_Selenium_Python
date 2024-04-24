from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class AccountPage(BasePage):
    _url = "https://magento.softwaretestingboard.com/customer/account/"
    __product_image = (By.CLASS_NAME, "product-image-photo")
    __remove_item = (By.XPATH, "//form[@id='wishlist-view-form']//ol[@class='product-items']/li[@class='product-item']/div[@class='product-item-info']//a[@title='Remove Item']")

    def __init__(self, driver: WebDriver):
        self._driver = driver

    @property
    def current_url(self) -> str:
        return self._driver.current_url

    @property
    def expected_url(self) -> str:
        return self._url

    def delete_product_from_wish_list(self):
        super()._hover_over(self.__product_image)
        super()._click(self.__remove_item)


