import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

class BaseTest:
    @pytest.fixture(scope="class")
    def driver(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        driver.quit()



