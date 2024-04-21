import time
from page_objects.order_women import OrderWomen
from tests.conftest import driver


class TestOrderWomen:
    def test_order(self, driver):
        order_women = OrderWomen(driver)
        order_women.go_to_tops()
        time.sleep(10)
