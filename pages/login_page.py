from selenium.webdriver.common.by import By

from base.webdriver_keywords import WebdriverKeywords


class LoginPage(WebdriverKeywords):

    def __init__(self, driver):
        super().__init__(driver)

    def enter_username(self, username):
        self.type_by_locator((By.NAME, "username"), username)

    def enter_password(self, password):
        self.type_by_locator((By.NAME, "password"), password)

    def click_on_login(self):
        self.click_by_locator((By.XPATH, "//button[@type='submit']"))

    @property
    def get_invalid_error_message(self):
        return self.driver.find_element(By.XPATH, "//p[normalize-space()='Invalid credentials']").text

    @property
    def get_username_placeholder(self):
        return self.driver.find_element(By.NAME, "username").get_attribute("placeholder")

    @property
    def get_password_placeholder(self):
        return self.driver.find_element(By.NAME, "password").get_attribute("placeholder")
