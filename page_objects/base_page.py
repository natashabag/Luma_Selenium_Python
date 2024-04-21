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

    def _click(self, locator: tuple, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).click()

    def _scroll_into_view(self, locator):
        element = self._find(locator)
        ActionChains(self._driver).move_to_element(element).perform()

    def _wait_for_element_to_load(self, locator):
        wait_to_load = wait(self._driver, 15)
        element = wait_to_load.until(ec.visibility_of_element_located(locator))
        return element