from base.webdriver_listener import WebdriverWrapper
from assertpy import assert_that
from selenium.webdriver.common.by import By


class TestLogin(WebdriverWrapper):
    def test_valid_login(self):
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        actual_header = self.driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']").text
        assert_that("Dashboard").is_equal_to(actual_header)

    def test_invalid_login(self):
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin12345")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        actual_error = self.driver.find_element(By.XPATH, "//p[normalize-space()='Invalid credentials']").text
        assert_that("Invalid credentials").is_equal_to(actual_error)


class TestLoginUi(WebdriverWrapper):
    def test_title(self):
        actual_title = self.driver.title
        # assert actual_title == "OrangeHRM"
        assert_that("OrangeHRM").is_equal_to(actual_title)

    def test_header(self):
        actual_header = self.driver.find_element(By.XPATH, "//h5[text()='Login']").text
        assert_that("Login").is_equal_to(actual_header)
