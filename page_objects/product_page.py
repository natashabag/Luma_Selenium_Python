import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class ProductPage(BasePage):
    __url = "https://magento.softwaretestingboard.com/"
    __women_button = (By.XPATH, "//span[text()='Women']")
    __top_link = (By.XPATH, "//a[text()='Tops']")
    __breathe_easy_tank = (By.CSS_SELECTOR, "img[alt='Breathe-Easy Tank']")
    __antonia_racer_tank = (By.CSS_SELECTOR, "img[alt='Antonia Racer Tank']")
    __s_size = (By.CSS_SELECTOR, "#option-label-size-143-item-167")
    __color_pink = (By.CSS_SELECTOR, "#option-label-color-93-item-57")
    __color_white = (By.CSS_SELECTOR, "#option-label-color-93-item-59")
    __add_to_cart_button = (By.ID, "product-addtocart-button")
    __cart = (By.CSS_SELECTOR, ".action.showcart")
    __message = (By.XPATH, '//*[@role="alert"]/div/div')
    __proceed_to_checkout_button = (By.ID, "top-cart-btn-checkout")
    __update_cart_button = (By.ID, "product-updatecart-button")
    __add_to_compare_button = (By.CSS_SELECTOR, ".product-addto-links > .action.tocompare > span")
    __compare_products_button = (By.XPATH, "//body//ul[@class='compare wrapper']/li/a[@title='Compare Products']")
    __page_title = (By.XPATH, "/html//main[@id='maincontent']//span[@class='base']")
    __product_added_message = (By.XPATH, "//main[@id='maincontent']//div[@role='alert']/div/div")
    __search_field = (By.ID, "search")

    # review:
    __add_review_link = (By.CSS_SELECTOR, ".action.add")
    __rating = (By.XPATH, "//*[@id='Rating_3_label']/span")
    __review_tab = (By.ID, "tab-label-reviews-title")
    __submit_review_button = (By.XPATH, "//form[@id='review-form']//button[@type='submit']/span[.='Submit Review']")
    __nickname_field = (By.ID, "nickname_field")
    __summary_field = (By.ID, "summary_field")
    __review_field = (By.ID, "review_field")

    __product = "shorts"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def go_to_women(self):
        super()._open_url(self.__url)
        super()._click(self.__women_button)
        super()._click(self.__top_link)

    def add_top(self):
        super()._scroll_into_view(self.__add_to_cart_button)
        super()._click(self.__s_size)
        super()._click(self.__color_pink)
        super()._click(self.__add_to_cart_button)


    def compare(self):
        super()._scroll_into_view(self.__add_to_compare_button)
        super()._click(self.__add_to_compare_button)

    def go_to_compare(self):
        super()._scroll_into_view(self.__compare_products_button)
        super()._click(self.__compare_products_button)
    def view_product(self):
        super()._click(self.__breathe_easy_tank)

    def view_product2(self):
        super()._click(self.__antonia_racer_tank)

    def get_page_title(self):
        return super()._get_text(self.__page_title)

    def select_white(self):
        super()._scroll_into_view(self.__color_white)
        super()._click(self.__color_white)
        super()._scroll_into_view(self.__update_cart_button)
        super()._click(self.__update_cart_button)

    def check_if_success_message_displayed(self):
        time.sleep(3)
        super()._scroll_into_view(self.__product_added_message)
        return super()._is_visible(self.__product_added_message)

    def search_for_product(self):
        super()._type(self.__search_field, self.__product)
        super()._press_enter(self.__search_field)

    def get_product(self):
        return self.__product


    def see_hover(self):
        super()._open_url(self.__url)
        super()._hover_over(self.__women_button)

    def leave_review(self):
        super()._click(self.__add_review_link)
        time.sleep(2)
        super()._wait_for_element_to_load(self.__nickname_field)
        super()._scroll_into_view(self.__review_field)
        super()._type(self.__nickname_field, "Nickname")
        super()._type(self.__summary_field, "Summary")
        super()._type(self.__review_field, "Review")
        super()._hover_over(self.__rating)
        super()._click(self.__rating)
        super()._click(self.__submit_review_button)



        #super()._wait_for_element_to_load(self.__message)
        #super()._scroll_into_view(self.__cart)
        #super()._click(self.__cart)
        #super()._click(self.__proceed_to_checkout_button)


