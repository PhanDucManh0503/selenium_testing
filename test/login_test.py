import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_test import BaseTest as base_test

class Test_login(base_test):

    def test_login(self, driver):
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.implicitly_wait(5)
        user_name = driver.find_element(By.NAME, "username")
        user_name.send_keys("Admin")
        password = driver.find_element(By.NAME, "password")
        password.send_keys("admin123")
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
        driver.implicitly_wait(5)
        print(driver.title)
        assert "OrangeHRM" in driver.title


    def test_login(self, driver):
        self.login(driver, "Admin", "admin123")
        print(driver.title)
        assert "OrangeHRM" in driver.title
    