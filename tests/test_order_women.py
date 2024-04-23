import time
from page_objects.order_women import OrderWomen
from tests.conftest import driver


class TestOrderWomen:
    def test_order(self, driver):
        order_women = OrderWomen(driver)
        order_women.go_to_tops()
        time.sleep(10)

    def test_compare(self, driver):
        order_women = OrderWomen(driver)
        order_women.go_to_women()
        order_women.view_product()
        order_women.compare()
        order_women.go_to_women()
        order_women.view_product2()
        order_women.compare()
        time.sleep(3)
        order_women.go_to_compare()
        time.sleep(3)
        assert order_women.get_compare_page_title() == "Compare Products", "Unexpected error message"

    def test_leave_review(self, driver):
        product_page = OrderWomen(driver)
        product_page.go_to_women()
        product_page.view_product()
        product_page.leave_review()
        time.sleep(3)


