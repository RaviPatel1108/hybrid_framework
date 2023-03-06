import pytest
from selenium import webdriver
from assertpy import assert_that
from selenium.webdriver.common.by import By


class WebdriverWrapper:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        yield
        self.driver.quit()


class TestLogin(WebdriverWrapper):
    def test_valid_login(self):
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        actual_header = self.driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']").text
        assert_that("Dashboard").is_equal_to(actual_header)


class TestLoginUi(WebdriverWrapper):
    def test_title(self):
        actual_title = self.driver.title
        # assert actual_title == "OrangeHRM"
        assert_that("OrangeHRM").is_equal_to(actual_title)

    def test_header(self):
        actual_header = self.driver.find_element(By.XPATH, "//h5[text()='Login']").text
        assert_that("Login").is_equal_to(actual_header)
