import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    print(f"creating {browser} driver")
    if browser == "chrome":
        my_driver = webdriver.Chrome()
    elif browser == "firefox":
        my_driver = webdriver.Firefox()
    else:
        raise TypeError(f"Expected 'chrome' or 'firefox' but got {browser}")
    yield my_driver
    print(f"closing {browser} driver")
    my_driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser to execute tests(chrome or firefox")
