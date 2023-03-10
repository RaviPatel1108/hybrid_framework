import pytest
from selenium.webdriver.common.by import By
from assertpy import assert_that
from base.webdriver_listener import WebdriverWrapper
from utilities.data_source import test_add_employee_data
from utilities.data_source import test_invalid_file_upload
import time


class TestAddEmployee(WebdriverWrapper):
    @pytest.mark.parametrize("username, password, firstname, middlename, lastname, expected_name1, expected_first_name",
                             test_add_employee_data)
    def test_add_valid_employee(self, username, password, firstname, middlename, lastname, expected_name1,
                                expected_first_name):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.XPATH, "//span[text()='PIM']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Add Employee']").click()
        self.driver.find_element(By.NAME, "firstName").send_keys(firstname)
        self.driver.find_element(By.NAME, "middleName").send_keys(middlename)
        self.driver.find_element(By.NAME, "lastName").send_keys(lastname)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(20)

        actual_employee_name = self.driver.find_element(By.XPATH, "//div[contains(@class,'employee-name')]").text
        assert_that(expected_name1).is_equal_to(actual_employee_name)
        actual_first_name = self.driver.find_element(By.NAME, "firstName").get_attribute("value")
        assert_that(expected_first_name).is_equal_to(actual_first_name)

    @pytest.mark.parametrize("username, password, filepath, expected_error",
                             test_invalid_file_upload)
    def test_invalid_profile_upload(self, username, password, filepath, expected_error):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.XPATH, "//span[text()='PIM']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Add Employee']").click()
        self.driver.find_element(By.XPATH, "//input[@type='file']").send_keys(filepath)
        actual_error = self.driver.find_element(By.XPATH, "//span[contains(normalize-space(), 'not allowed')]").text
        assert_that(expected_error).is_equal_to(actual_error)
