from page_objects.base_page import BasePage


class AccountPage(BasePage):
    __url = "https://magento.softwaretestingboard.com/customer/account/"

    def current_url(self) -> str:
        return self.__url


