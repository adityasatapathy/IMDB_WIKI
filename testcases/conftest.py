import time
import pytest
from selenium import webdriver
from base.baseclass import Baseclass1


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope='class')
def setup_browser(request):
    base = Baseclass1()
    driver = webdriver.Chrome(executable_path=(base.configReader("cred", "driver_obj")))
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()