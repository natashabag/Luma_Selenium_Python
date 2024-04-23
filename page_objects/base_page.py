from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _open_url(self, url: str):
        self._driver.get(url)

    def _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)

    def _wait_until_element_is_visible(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))

    def _element_is_clickable(self, locator, timeout=5):
        return wait(self._driver, timeout).until(ec.element_to_be_clickable(locator))
    def _click(self, locator: tuple, time: int = 10):
        self._element_is_clickable(locator, time)
        self._find(locator).click()

    def _scroll_into_view(self, locator):
        element = self._find(locator)
        ActionChains(self._driver).move_to_element(element).perform()

    def _wait_for_element_to_load(self, locator):
        wait_to_load = wait(self._driver, 15)
        element = wait_to_load.until(ec.visibility_of_element_located(locator))
        return element

    def _type(self, locator: tuple, text: str, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).send_keys(text)

    def select_option_from_dropdown(self, locator, text):
        select_element = self._find(locator)
        select = Select(select_element)
        select.select_by_visible_text(text)

    def _get_text(self, locator: tuple, time: int = 10) -> str:
        return self._find(locator).text

    def _hover_over(self, locator, time: int = 10):
        self._element_is_clickable(locator, time)
        element = self._find(locator)
        ActionChains(self._driver).move_to_element(element).perform()

    def _is_visible(self, locator):
        self._wait_for_element_to_load(locator)
        return self._find(locator).is_displayed()
