from selenium.webdriver.common.by import By
from assertpy import assert_that
from base.webdriver_listener import WebdriverWrapper
import time


class TestAddEmployee(WebdriverWrapper):
    def test_add_valid_employee(self):
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.XPATH, "//span[text()='PIM']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Add Employee']").click()
        self.driver.find_element(By.NAME, "firstName").send_keys("Ravi")
        self.driver.find_element(By.NAME, "lastName").send_keys("Patel")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(20)

        actual_employee_name = self.driver.find_element(By.XPATH, "//div[contains(@class,'employee-name')]").text
        assert_that("Ravi Patel").is_equal_to(actual_employee_name)
        actual_first_name = self.driver.find_element(By.NAME, "firstName").get_attribute("value")
        assert_that("Ravi").is_equal_to(actual_first_name)
        actual_last_name = self.driver.find_element(By.NAME, "lastName").get_attribute("value")
        assert_that("Patel").is_equal_to(actual_last_name)


